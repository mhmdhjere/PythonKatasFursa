import unittest
from katas.true_counter import count_true_values

class TestCountTrueValues(unittest.TestCase):

    def test_all_true(self):
        self.assertEqual(count_true_values([True, True, True]), 3)

    def test_all_false(self):
        self.assertEqual(count_true_values([False, False, False]), 0)

    def test_mixed_values(self):
        self.assertEqual(count_true_values([True, False, True, False]), 2)

    def test_empty_list(self):
        self.assertEqual(count_true_values([]), 0)

    def test_truthy_values_not_counted(self):
        self.assertEqual(count_true_values([1, "True", True, 0, None]), 1)

    def test_only_true_counted(self):
        self.assertEqual(count_true_values([True, True is True, False is False, 1 == 1, 0]), 4)

if __name__ == "__main__":
    unittest.main()

