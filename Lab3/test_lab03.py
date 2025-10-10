import unittest
from lab03 import gen_bin_tree


class TestGenBinTree(unittest.TestCase):

    def test_height_0(self):
        # Тест для высоты 0
        tree = gen_bin_tree(0, 1)
        self.assertEqual(tree, [1])

    def test_height_1(self):
        # Тест для высоты 1
        tree = gen_bin_tree(1, 1)
        self.assertEqual(tree, [1, [2], [4]])

    def test_height_2(self):
        # Тест для высоты 2
        tree = gen_bin_tree(2, 1)
        self.assertEqual(tree, [1, [2, [4], [5]], [4, [8], [7]]])


if __name__ == '__main__':
    unittest.main()
