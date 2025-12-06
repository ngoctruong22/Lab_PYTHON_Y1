import unittest
import io

import requests

from Lab7.currencies import get_currencies
from Lab7.decorators import logger

class TestStreamWrite(unittest.TestCase):

    def setUp(self):
        self.stream = io.StringIO()

        @logger(handle=self.stream)
        def wrapped_success():
            return get_currencies(['USD'], url="https://www.cbr-xml-daily.ru/daily_json.js")

        self.wrapped_success = wrapped_success

        @logger(handle=self.stream)
        def wrapped_error():
            return get_currencies(['USD'], url="https://invalid")

        self.wrapped_error = wrapped_error


    def test_logging_success(self):
        self.wrapped_success()
        logs_success = self.stream.getvalue()

        self.assertIn("[INFO] start", logs_success)
        self.assertIn("[INFO] success", logs_success)

    def test_logging_error(self):
        with self.assertRaises(requests.exceptions.RequestException):
            self.wrapped_error()

        logs = self.stream.getvalue()

        self.assertIn("ERROR", logs)
        self.assertIn("API недоступен", logs)


if __name__ == "__main__":
    unittest.main(argv=[''], verbosity=2, exit=False)