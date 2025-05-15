import unittest
from katas.is_valid_parentheses import is_valid_parentheses

class TestValidParentheses(unittest.TestCase):

    def test_valid_cases(self):
        self.assertTrue(is_valid_parentheses("()"))
        self.assertTrue(is_valid_parentheses("()[]{}"))
        self.assertTrue(is_valid_parentheses("{[()]}"))
        self.assertTrue(is_valid_parentheses("(([]){})"))

    def test_invalid_cases(self):
        self.assertFalse(is_valid_parentheses("(]"))
        self.assertFalse(is_valid_parentheses("([)]"))
        self.assertFalse(is_valid_parentheses("({[})"))
        self.assertFalse(is_valid_parentheses("((("))
        self.assertFalse(is_valid_parentheses(")))"))

    def test_edge_cases(self):
        self.assertTrue(is_valid_parentheses(""))  # empty string
        self.assertFalse(is_valid_parentheses(")("))  # closing before opening

if __name__ == "__main__":
    unittest.main()

