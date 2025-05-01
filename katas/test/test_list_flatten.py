import unittest
from katas.list_flatten import flatten_list


class TestListFlatten(unittest.TestCase):
    def test_list_flatten(self):
        self.assertEqual(flatten_list([10, 3, 5, 6, 20, -2]), [10, 3, 5, 6, 20, -2])
        self.assertEqual(flatten_list([]), [])
        self.assertEqual(flatten_list([[[[[[[1]]]]]]]), [1])
        self.assertEqual(flatten_list([1,[2, 3],[4, [5, 6]],7]),[1, 2, 3, 4, 5, 6, 7])
