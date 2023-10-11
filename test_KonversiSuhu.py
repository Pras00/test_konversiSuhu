import unittest
from konversiSuhu import KonversiSuhu

class TestKonversiSuhu(unittest.TestCase):
    def setUp(self):
        self.konversi = KonversiSuhu()

    def test_celsius_ke_reamur(self):
        self.assertEqual(self.konversi.celsius_ke_reamur(0), 0.0)
        self.assertEqual(self.konversi.celsius_ke_reamur(100), 80.0)

    def test_celsius_ke_fahrenheit(self):
        self.assertEqual(self.konversi.celsius_ke_fahrenheit(0), 32.0)
        self.assertEqual(self.konversi.celsius_ke_fahrenheit(100), 212.0)

    def test_celsius_ke_kelvin(self):
        self.assertEqual(self.konversi.celsius_ke_kelvin(0), 273.0)
        self.assertEqual(self.konversi.celsius_ke_kelvin(100), 373.0)

    def test_reamur_ke_celsius(self):
        self.assertEqual(self.konversi.reamur_ke_celsius(0), 0.0)
        self.assertEqual(self.konversi.reamur_ke_celsius(80), 100.0)

    def test_reamur_ke_fahrenheit(self):
        self.assertEqual(self.konversi.reamur_ke_fahrenheit(0), 32.0)
        self.assertEqual(self.konversi.reamur_ke_fahrenheit(80), 212.0)

    def test_reamur_ke_kelvin(self):
        self.assertEqual(self.konversi.reamur_ke_kelvin(0), 273.0)
        self.assertEqual(self.konversi.reamur_ke_kelvin(80), 373,0)

    def test_fahrenheit_ke_celsius(self):
        self.assertEqual(self.konversi.fahrenheit_ke_celsius(32), 0.0)
        self.assertEqual(self.konversi.fahrenheit_ke_celsius(212), 100.0)

    def test_fahrenheit_ke_kelvin(self):
        self.assertEqual(self.konversi.fahrenheit_ke_kelvin(32), 273.0)
        self.assertEqual(self.konversi.fahrenheit_ke_kelvin(212), 373.0)

    def test_fahrenheit_ke_reamur(self):
        self.assertEqual(self.konversi.fahrenheit_ke_reamur(32), 0.0)
        self.assertEqual(self.konversi.fahrenheit_ke_reamur(212), 80.0)

    def test_kelvin_ke_celsius(self):
        self.assertEqual(self.konversi.kelvin_ke_celsius(273), 0.0)
        self.assertEqual(self.konversi.kelvin_ke_celsius(373), 101.0)

    def test_kelvin_ke_fahrenheit(self):
        self.assertEqual(self.konversi.kelvin_ke_fahrenheit(273), 32.0)
        self.assertEqual(self.konversi.kelvin_ke_fahrenheit(373), 212.0)

    def test_kelvin_ke_reamur(self):
        self.assertEqual(self.konversi.kelvin_ke_reamur(273), 0.0)
        self.assertEqual(self.konversi.kelvin_ke_reamur(373), 81.0)

if __name__ == '__main__':
    unittest.main()
