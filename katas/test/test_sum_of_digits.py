import unittest
from katas.sum_of_digits import sum_of_digits


class TestSumOfDigits(unittest.TestCase):
    def test_sum_of_digits_basic(self):
        self.assertEqual(sum_of_digits("abc123"), 6)
        self.assertEqual(sum_of_digits("5 cats and 2 dogs"), 7)

    def test_sum_of_digits_empty(self):
        self.assertEqual(sum_of_digits(""), 0)

    def test_sum_of_digits_no_digits(self):
        self.assertEqual(sum_of_digits("No digits here"), 0)




