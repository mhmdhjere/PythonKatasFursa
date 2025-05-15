import unittest
from katas.is_valid_git_tree import has_cycle, has_one_root, is_valid_git_tree  # Replace 'your_module' with the actual filename (without .py)

class TestGitTreeFunctions(unittest.TestCase):

    def test_has_cycle(self):
        graph = {
            "A": ["B"],
            "B": ["C"],
            "C": ["A"]
        }
        self.assertTrue(has_cycle(graph))

    def test_has_multiple_roots(self):
        tree_map = {
            "A": ["B"],
            "C": ["D"]
        }
        self.assertFalse(has_one_root(tree_map))

    def test_has_multiple_parents(self):
        tree_map = {
            "A": ["B"],
            "B": [],
            "C": ["B"]  # B has two parents
        }
        self.assertFalse(has_one_root(tree_map))

    def test_valid_git_tree(self):
        tree_map = {
            "A": ["B", "C"],
            "B": ["D"],
            "C": [],
            "D": []
        }
        self.assertTrue(is_valid_git_tree(tree_map))

    def test_is_not_valid_git_tree(self):
        tree_map = {
            "A": ["B"],
            "B": ["C"],
            "C": ["A"]
        }
        self.assertFalse(is_valid_git_tree(tree_map))

        tree_map = {
            "A": ["B"],
            "B": [],
            "C": ["B"]  # B has two parents
        }
        self.assertFalse(is_valid_git_tree(tree_map))

        tree_map = {
            "A": ["B"],
            "C": ["D"]
        }
        self.assertFalse(is_valid_git_tree(tree_map))


if __name__ == '__main__':
    unittest.main()
