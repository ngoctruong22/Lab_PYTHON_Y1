import unittest
from unittest.mock import MagicMock

from controllers.currencycontroller import CurrencyController


class TestCurrencyController(unittest.TestCase):
    def test_list_currencies(self):
        mock_db = MagicMock()
        mock_db.list.return_value = [{"id": 1, "char_code": "USD", "value": 90}]
        controller = CurrencyController(mock_db)
        result = controller.list_currencies()
        self.assertEqual(result[0]["char_code"], "USD")
        mock_db.list.assert_called_once()


if __name__ == "__main__":
    unittest.main()
