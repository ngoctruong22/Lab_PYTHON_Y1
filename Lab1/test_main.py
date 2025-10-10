import unittest
from main import twoSum


class TestTwoSum(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(twoSum([2, 7, 11, 15], 9), [0, 1])

    def test_example2(self):
        self.assertEqual(twoSum([3, 2, 4], 6), [1, 2])

    def test_example3(self):
        self.assertEqual(twoSum([3, 3], 6), [0, 1])

    def test_negative(self):
        self.assertEqual(twoSum([-1, -3, -2, -4], -6), [2, 3])

    def test_empty(self):
        self.assertEqual(twoSum([], 1), None)

    def test_element_type(self):
        self.assertIsNone(twoSum(['a', 2, 4], 6))

    def test_no_answer(self):
        self.assertEqual(twoSum([1, 2, 3, 4, 5], 10), None)

    def test_one_element(self):
        self.assertEqual(twoSum([5], 5), None)

    def test_more_than_answer(self):
        self.assertEqual(twoSum([2, 2, 2, 2, 2], 4), [0, 1])


if __name__ == '__main__':
    unittest.main()
