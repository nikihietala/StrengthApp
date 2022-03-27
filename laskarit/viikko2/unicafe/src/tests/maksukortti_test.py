import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)
    
    def test_konstruktori_asettaa_saldon_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")

    def test_kortille_voi_ladata_rahaa(self):
        self.maksukortti.lataa_rahaa(400)
        self.assertEqual(str(self.maksukortti), "saldo: 4.1")
    
    def test_kortilta_voi_ottaa_rahaa_jos_rahat_riittaa(self):
        self.maksukortti.ota_rahaa(5)
        self.assertEqual(str(self.maksukortti), "saldo: 0.05")
    
    def test_kortilta_ei_voi_ottaa_rahaa_jos_rahat_ei_riita(self):
        self.maksukortti.ota_rahaa(15)
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")
    
    def test_jos_rahat_riittaa(self):
        self.assertEqual(self.maksukortti.ota_rahaa(5), True)
    
    def test_jos_rahat_ei_riita(self):
        self.assertEqual(self.maksukortti.ota_rahaa(20), False)



