import unittest
from katas.is_unique_str import is_unique


class TestHelloWorld(unittest.TestCase):
    def test_is_unique_str(self):
        self.assertEqual(is_unique("Hello"), False)
        self.assertEqual(is_unique("World"), True)
        self.assertEqual(is_unique("Python"), True)
        self.assertEqual(is_unique("Unique"), False)
