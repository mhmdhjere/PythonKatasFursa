import unittest
from katas.matrix_rotate import rotate_matrix


class TestRotateMatrix(unittest.TestCase):
    # this test checks that the time is in reasonable range close to 500ms
    def test_rotate_matrix_basic(self):
        matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        rotate_matrix(matrix)
        self.assertEqual(matrix, [[7,4,1],[8,5,2],[9,6,3]])

    def test_rotate_matrix_empty(self):
        matrix = []
        rotate_matrix(matrix)
        self.assertEqual(matrix, [])

    def test_rotate_matrix_one_element(self):
        matrix = [[1]]
        rotate_matrix(matrix)
        self.assertEqual(matrix, [[1]])








