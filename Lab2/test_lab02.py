import unittest
from lab02 import guess_number


class MyTestCase(unittest.TestCase):
    # Таргет попадает
    def test_target_found(self):
        self.assertEqual(guess_number(3, [1, 2, 3, 4], type='seq'), [3, 3])
        self.assertEqual(guess_number(4, [1, 2, 3, 4, 5], type='bin'), [4, 2])

    # Таргет не попадает
    def test_target_not_found(self):
        self.assertEqual(guess_number(10, [1, 2, 3], type='seq'), [None, 3])
        self.assertEqual(guess_number(10, [1, 2, 3, 4, 5], type='bin'), [None, 3])

    # Диапозон пустой
    def test_empty_range(self):
        self.assertEqual(guess_number(1, [], type='seq'), [None, 0])
        self.assertEqual(guess_number(1, [], type='bin'), [None, 0])

    # Диапозон из 1 числа
    def test_single_element_found(self):
        self.assertEqual(guess_number(5, [5], type='seq'), [5, 1])
        self.assertEqual(guess_number(5, [5], type='bin'), [5, 1])

    def test_single_element_not_found(self):
        self.assertEqual(guess_number(3, [5], type='seq'), [None, 1])
        self.assertEqual(guess_number(3, [5], type='bin'), [None, 1])

    # Input введен сначала большой потом малый
    def test_reverse_input_range(self):
        d = list(range(10, 5))  # empty range
        self.assertEqual(guess_number(7, d, type='seq'), [None, 0])

    # Input - float, string который можно преобразовать в int
    def test_convertible_input(self):
        self.assertEqual(guess_number(int(float(5.0)), [1, 2, 3, 4, 5], type='seq'), [5, 5])
        self.assertEqual(guess_number(int("3"), [1, 2, 3, 4, 5], type='bin'), [3, 1])

    # Input - float, string который нельзя преобразовать в int
    def test_non_convertible_input(self):
        with self.assertRaises(ValueError):
            int("1a")
        with self.assertRaises(ValueError):
            int("5.5.5")

    # Range от отрицательных до положительных
    def test_negative_to_positive_range(self):
        d = list(range(-10, 11))
        self.assertEqual(guess_number(-3, d, type='bin'), [-3, 3])
        self.assertEqual(guess_number(0, d, type='seq'), [0, 11])

    # Список с повторяющимися элементами
    def test_range_with_duplicates(self):
        lst = [1, 2, 3, 3, 3, 3, 4, 5]
        self.assertEqual(guess_number(3, lst, type='seq'), [3, 3])
        self.assertEqual(guess_number(3, lst, type='bin'), [3, 1])

    # список не отсортирован
    def test_unsorted_range_bin(self):
        d = [5, 3, 1, 2, 4]
        res = guess_number(3, d, type='bin')
        self.assertTrue(res[0] is None or res[0] != 3)  # binary search не работает


if __name__ == '__main__':
    unittest.main()
