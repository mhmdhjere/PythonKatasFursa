import unittest
from katas.list_diff import find_difference


class TestListDiff(unittest.TestCase):
    def test_list_diff(self):
        self.assertEqual(find_difference([10, 3, 5, 6, 20, -2]), 22)
        self.assertEqual(find_difference([]), 0)
        self.assertEqual(find_difference([5]),0)
