import unittest
from katas.test_case_grouping import group_test_cases

class TestGroupTestCases(unittest.TestCase):

    def test_single_group_size(self):
        input_data = [3, 3, 3, 3, 3, 3]
        expected = [[0, 1, 2], [3, 4, 5]]
        self.assertEqual(group_test_cases(input_data), expected)

    def test_mixed_group_sizes(self):
        input_data = [3, 3, 3, 3, 3, 1, 3]
        expected = [[0, 1, 2], [3, 4, 6], [5]]
        self.assertEqual(group_test_cases(input_data), expected)

    def test_all_groups_of_size_1(self):
        input_data = [1, 1, 1, 1]
        expected = [[0], [1], [2], [3]]
        self.assertEqual(group_test_cases(input_data), expected)

    def test_all_groups_of_size_2(self):
        input_data = [2, 2, 2, 2]
        expected = [[0, 1], [2, 3]]
        self.assertEqual(group_test_cases(input_data), expected)

    def test_non_sequential_sizes(self):
        input_data = [2, 1, 3, 3, 3, 2]
        expected = [[0, 5], [1], [2, 3, 4]]
        self.assertEqual(group_test_cases(input_data), expected)

    def test_empty_input(self):
        input_data = []
        expected = []
        self.assertEqual(group_test_cases(input_data), expected)

    def test_insufficient_members_to_complete_group(self):
        # According to function logic, incomplete groups should not appear, but since input guarantees
        # proper groupings per problem constraints (assumed), we don't test for broken cases.
        input_data = [2, 2, 2]
        expected = [[0, 1], [2]]
        self.assertEqual(group_test_cases(input_data), expected)

if __name__ == "__main__":
    unittest.main()

