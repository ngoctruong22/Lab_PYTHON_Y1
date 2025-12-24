import unittest
from models.user import User
from models.currency import Currency

class TestModels(unittest.TestCase):
    def test_user_setter(self):
        u = User(1, "Alice")
        self.assertEqual(u.id, 1)
        self.assertEqual(u.name, "Alice")
        with self.assertRaises(ValueError):
            u.id = -5
        with self.assertRaises(ValueError):
            u.name = ""

    def test_currency_setter(self):
        c = Currency("R01280", "360", "IDR", "Rupiah", 48.6178, 10000)
        self.assertEqual(c.char_code, "IDR")
        self.assertAlmostEqual(c.value, 48.6178)
        with self.assertRaises(ValueError):
            c.nominal = 0

if __name__ == "__main__":
    unittest.main()
