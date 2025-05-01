import unittest
from katas.reduce_list import reduce_array


class TestReduceList(unittest.TestCase):
    def test_reduce_array_basic(self):
        nums = [10, 15, 7, 20, 25]
        reduce_array(nums)
        self.assertEqual(nums, [10, 5, -8, 13, 5])

    def test_reduce_array_empty(self):
        nums = []
        reduce_array(nums)
        self.assertEqual(nums, [])

    def test_reduce_array_one_element(self):
        nums = [5]
        reduce_array(nums)
        self.assertEqual(nums, [5])


