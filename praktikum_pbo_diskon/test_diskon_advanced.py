import unittest
from diskon_service_advanced import DiskonCalculator

class TestDiskonAdvanced(unittest.TestCase):

    def setUp(self):
        self.calc = DiskonCalculator()

    def test_float_diskon(self):
        hasil = self.calc.hitung_diskon(999, 33)
        self.assertAlmostEqual(hasil, 736.263, places=2)

    def test_harga_awal_nol(self):
        hasil = self.calc.hitung_diskon(0, 10)
        self.assertEqual(hasil, 0.0)


if __name__ == "__main__":
    unittest.main()
