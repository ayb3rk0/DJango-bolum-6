from django.contrib import admin
from .models import Soru, Secenek

# 1. Seçenekleri sorunun içine gömmek için bir "satır içi" sınıfı oluşturuyoruz
class SecenekEkleme(admin.TabularInline):
    model = Secenek
    extra = 3  # Soru eklerken altta otomatik 3 tane boş seçenek kutusu açar

# 2. Soru panelinin nasıl görüneceğini ayarlıyoruz
class SoruAdmin(admin.ModelAdmin):
    # Formdaki alanların sırasını ve gruplarını belirliyoruz
    fieldsets = [
        (None, {"fields": ["soru_metni"]}),
        ("Tarih Bilgisi", {"fields": ["yayin_tarihi"], "classes": ["collapse"]}),
    ]
    inlines = [SecenekEkleme] # Seçenekleri buraya bağladık
    
    # Listeleme sayfasındaki sütunlar
    list_display = ["soru_metni", "yayin_tarihi", "yakin_zamanda_yayinlandi_mi"]
    
    # Sağ tarafa filtreleme paneli
    list_filter = ["yayin_tarihi"]
    
    # Üst tarafa arama kutusu
    search_fields = ["soru_metni"]

# 3. Hazırladığımız bu ayarları Django'ya kaydediyoruz
admin.site.register(Soru, SoruAdmin)