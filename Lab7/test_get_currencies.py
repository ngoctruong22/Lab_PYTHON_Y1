import unittest
import requests
from Lab7.currencies import get_currencies

MAX_R_VALUE = 1000


# Тесты
class TestGetCurrencies(unittest.TestCase):
    def test_currency_usd(self):
        """
              Проверяет наличие ключа в словаре и значения этого ключа
            """
        currency_list = ['USD']
        currency_data = get_currencies(currency_list)

        self.assertIn(currency_list[0], currency_data)
        self.assertIsInstance(currency_data['USD'], float)
        self.assertGreaterEqual(currency_data['USD'], 0)
        self.assertLessEqual(currency_data['USD'], MAX_R_VALUE)

    def test_nonexist_code(self):
        self.assertIn("Код валюты", get_currencies(['XYZ'])['XYZ'])
        self.assertIn("XYZ", get_currencies(['XYZ'])['XYZ'])
        self.assertIn("не найден", get_currencies(['XYZ'])['XYZ'])

    def test_get_currency_error(self):

        currency_list = ['USD']


        with self.assertRaises(requests.exceptions.RequestException):
            get_currencies(currency_list, url="https://")
        with self.assertRaises(ValueError):
            get_currencies(currency_list, url="https://www.cbr.ru/scripts/XML_daily.asp")
        with self.assertRaises(KeyError):
            get_currencies(currency_list, url="https://jsonplaceholder.typicode.com/users")
        with self.assertRaises(TypeError):
            get_currencies(currency_codes=1, url="https://www.cbr-xml-daily.ru/daily_json.js")


if __name__ == "__main__":
    unittest.main(argv=[''], verbosity=2, exit=False)


