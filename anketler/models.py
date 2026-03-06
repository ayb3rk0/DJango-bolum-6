import datetime
from django.db import models
from django.utils import timezone

class Soru(models.Model):
    soru_metni = models.CharField(max_length=200)
    yayin_tarihi = models.DateTimeField('yayınlanma tarihi')

    def __str__(self):
        return self.soru_metni

    # HATASI DÜZELTİLMİŞ TESTTEN GEÇEN FONKSİYON
    def yakin_zamanda_yayinlandi_mi(self):
        su_an = timezone.now()
        return su_an - datetime.timedelta(days=1) <= self.yayin_tarihi <= su_an

class Secenek(models.Model):
    soru = models.ForeignKey(Soru, on_delete=models.CASCADE)
    secenek_metni = models.CharField(max_length=200)
    oy_sayisi = models.IntegerField(default=0)

    def __str__(self):
        return self.secenek_metni