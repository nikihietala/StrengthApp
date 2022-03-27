import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti


class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()

    def test_luotu_paate_on_olemassa(self):
        self.assertNotEqual(self.kassapaate, None)
    
    def test_kassassa_oikea_rahamaara(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_myytyjen_lounaiden_maara_on_alussa_oikea(self):
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_edullinen_kateisosto_toimii_jos_rahat_riittaa(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(240), 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
        self.assertEqual(self.kassapaate.edulliset, 1)
    
    def test_edullinen_kateisosto_toimii_jos_rahaa_on_enemman(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(300), 60)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
        self.assertEqual(self.kassapaate.edulliset, 1)
    
    def test_edullinen_kateisosto_ei_toimi_jos_rahat_ei_riita(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(200), 200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_maukas_kateisosto_toimii_jos_rahat_riittaa(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(400), 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_maukas_kateisosto_toimii_jos_rahaa_on_enemman(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(500), 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_maukas_kateisosto_ei_toimi_jos_rahat_ei_riita(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(240), 240)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_edullinen_korttiosto_toimii_jos_rahat_riittaa(self):
        self.maksukortti = Maksukortti(1000)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), True)
        self.assertEqual(self.maksukortti.saldo, 760)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_maukas_korttiosto_toimii_jos_rahat_riittaa(self):
        self.maksukortti = Maksukortti(1000)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti), True)
        self.assertEqual(self.maksukortti.saldo, 600)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_edullinen_korttiosto_ei_toimi_jos_rahat_ei_riita(self):
        self.maksukortti = Maksukortti(100)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), False)
        self.assertEqual(self.maksukortti.saldo, 100)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_maukas_korttiosto_ei_toimi_jos_rahat_ei_riita(self):
        self.maksukortti = Maksukortti(300)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti), False)
        self.assertEqual(self.maksukortti.saldo, 300)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kortille_voi_ladata_rahaa(self):
        self.maksukortti = Maksukortti(100)
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 100)
        self.assertEqual(self.maksukortti.saldo, 200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100100)
    
    def test_kortille_ei_voi_ladata_negatiivista_summaa(self):
        self.maksukortti = Maksukortti(100)
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -100)
        self.assertEqual(self.maksukortti.saldo, 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)



    





        


