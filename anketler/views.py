from django.db.models import F
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone  # Zaman hesaplaması için gerekli modül
from .models import Soru, Secenek

class IndexView(generic.ListView):
    template_name = "anketler/index.html"
    context_object_name = "en_yeni_sorular"

    def get_queryset(self):
        # SİHİRLİ DOKUNUŞ: Sadece yayın tarihi "şu an"dan küçük veya eşit olanları getir.
        # Gelecekteki sorular artık ana sayfada görünmeyecek!
        return Soru.objects.filter(yayin_tarihi__lte=timezone.now()).order_by("-yayin_tarihi")[:5]

class DetayView(generic.DetailView):
    model = Soru
    template_name = "anketler/detay.html"

class SonuclarView(generic.DetailView):
    model = Soru
    template_name = "anketler/sonuclar.html"

def oy_ver(request, soru_id):
    soru = get_object_or_404(Soru, pk=soru_id)
    try:
        secilen_secenek = soru.secenek_set.get(pk=request.POST["secenek"])
    except (KeyError, Secenek.DoesNotExist):
        return render(request, "anketler/detay.html", {
            "soru": soru,
            "hata_mesaji": "Bir seçenek işaretlemediniz!",
        })
    else:
        secilen_secenek.oy_sayisi = F("oy_sayisi") + 1
        secilen_secenek.save()
        return HttpResponseRedirect(reverse("anketler:sonuclar", args=(soru.id,)))