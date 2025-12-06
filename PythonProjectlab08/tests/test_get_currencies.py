import unittest
import requests
from PythonProjectlab08.utils.currencies_api import get_currencies


class TestGetCurrencies(unittest.TestCase):

    def test_error_invalid_url(self):
        with self.assertRaises(requests.exceptions.RequestException):
            get_currencies(url="https://")

    def test_error_invalid_json(self):
        with self.assertRaises(ValueError):
            get_currencies(url="https://www.cbr.ru/scripts/XML_daily.asp")

    def test_error_missing_valute_key(self):
        with self.assertRaises(KeyError):
            get_currencies(url="https://jsonplaceholder.typicode.com/users")

    def test_success(self):
        date, currencies = get_currencies()
        self.assertIsInstance(date, str)
        self.assertTrue(len(currencies) > 0)
        self.assertTrue(hasattr(currencies[0], "char_code"))


if __name__ == "__main__":
    unittest.main()