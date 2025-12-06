import unittest
import io
from Lab7.decorators import logger


class TestDecorator(unittest.TestCase):

    def setUp(self):
        self.stream = io.StringIO()

        @logger(handle=self.stream)
        def test_function(x):
            return x * 2

        @logger(handle=self.stream)
        def error_function(x):
            raise ValueError("x error")

        self.test_function = test_function
        self.error_function = error_function

    def test_decorators(self):
        result = self.test_function(5)
        logs = self.stream.getvalue()

        self.assertEqual(result, 10)
        self.assertRegex(logs, r"\[INFO\] start")  # r: raw string
        self.assertRegex(logs, r"\[INFO\] success")
        self.assertRegex(logs, r"args=\(5,\)")
        self.assertRegex(logs, r"with result: 10 ")

    def test_decorators_error(self):
        with self.assertRaises(ValueError):
            self.error_function(5)

        logs_error = self.stream.getvalue()

        self.assertRegex(logs_error, r"\[INFO\] start")
        self.assertRegex(logs_error, r"args=\(5,\)")
        self.assertRegex(logs_error, r"\[ERROR\] error in")  #
        self.assertRegex(logs_error, r"args=\(5,\)")
        self.assertRegex(logs_error, r"ValueError: ")
        self.assertRegex(logs_error, r"x error")


if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=2, exit=False)
