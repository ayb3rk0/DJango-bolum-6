import datetime
from django.test import TestCase
from django.utils import timezone
from .models import Soru

class SoruModeliTestleri(TestCase):

    def test_gelecekteki_soru_ile_yakin_zaman_kontrolu(self):
        """
        yakin_zamanda_yayinlandi_mi() metodu, yayin_tarihi gelecekte olan
        sorular için False döndürmelidir.
        """
        # Şu andan 30 gün sonrasını ayarlıyoruz
        gelecek_zaman = timezone.now() + datetime.timedelta(days=30)
        gelecekteki_soru = Soru(yayin_tarihi=gelecek_zaman)
        
        # Gelecekteki bir soru için sonucun 'False' çıkmasını bekliyoruz!
        self.assertIs(gelecekteki_soru.yakin_zamanda_yayinlandi_mi(), False)