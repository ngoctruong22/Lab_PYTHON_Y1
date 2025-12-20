import unittest
import math
from integrate_threaded import integrate_threaded


class TestIntegrateThreads(unittest.TestCase):

    def test_cos(self):
        """Интеграл косинуса от 0 → π/2 = 1"""
        result = integrate_threaded(math.cos, 0, math.pi / 2, n_iter=1000)
        self.assertEqual(round(result,1), 1.0)

    def test_sin(self):
        """Интеграл синуса от 0 → π = 2"""
        result = integrate_threaded(math.sin, 0, math.pi, n_iter=1000)
        self.assertEqual(round(result,1), 2.0)
    def test_quadratic(self):
        """Интеграл x² от 0 до 1 = 1/3"""
        result = integrate_threaded(lambda x: x**2, 0, 1, n_iter=1000)
        self.assertEqual(round(result,2), 0.33)


if __name__ == "__main__":
    unittest.main()