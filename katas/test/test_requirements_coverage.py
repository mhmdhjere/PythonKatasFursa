import unittest
from katas.requirements_coverage import select_minimal_test_cases

class TestSelectMinimalTestCases(unittest.TestCase):

    def test_basic_case(self):
        test_cases = [
            [1, 2],
            [2, 3],
            [3, 4],
            [4, 5]
        ]
        result = select_minimal_test_cases(test_cases)
        # One possible minimal solution: [0, 2, 3] or [0, 1, 3]
        self.assertTrue(set(result).issubset({0, 1, 2, 3}))
        covered = set()
        for i in result:
            covered.update(test_cases[i])
        self.assertEqual(covered, {1, 2, 3, 4, 5})

    def test_single_covering_case(self):
        test_cases = [
            [1, 2, 3, 4, 5],
            [1],
            [2],
            [3, 4]
        ]
        result = select_minimal_test_cases(test_cases)
        self.assertEqual(result, [0])

    def test_no_overlap(self):
        test_cases = [
            [1],
            [2],
            [3],
            [4]
        ]
        result = select_minimal_test_cases(test_cases)
        self.assertCountEqual(result, [0, 1, 2, 3])

    def test_all_empty(self):
        test_cases = [
            [],
            [],
            []
        ]
        result = select_minimal_test_cases(test_cases)
        self.assertEqual(result, [])

    def test_some_empty(self):
        test_cases = [
            [],
            [1, 2],
            [],
            [2, 3],
            []
        ]
        result = select_minimal_test_cases(test_cases)
        covered = set()
        for i in result:
            covered.update(test_cases[i])
        self.assertEqual(covered, {1, 2, 3})

    def test_duplicates(self):
        test_cases = [
            [1, 2],
            [2, 3],
            [3, 1]
        ]
        result = select_minimal_test_cases(test_cases)
        # All requirements are {1, 2, 3}
        covered = set()
        for i in result:
            covered.update(test_cases[i])
        self.assertEqual(covered, {1, 2, 3})

if __name__ == "__main__":
    unittest.main()

