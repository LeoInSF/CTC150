import unittest

def zero_matrix(matrix):

    row_num = len(matrix)
    column_num = len(matrix[0])
    row_zeros = []
    column_zeros = []

    for row in range(0, row_num):

        for column in range(0, column_num):

            if matrix[row][column] == 0:
                row_zeros.append(row)
                column_zeros.append(column)

    for row in row_zeros:

        for column in range(0, column_num):
            matrix[row][column] = 0

    for column in column_zeros:
        for row in range(0, row_num):
            matrix[row][column] = 0

    return matrix


class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ([
            [1, 2, 3, 4, 0],
            [6, 0, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 0, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ], [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [11, 0, 13, 14, 0],
            [0, 0, 0, 0, 0],
            [21, 0, 23, 24, 0]
        ])
    ]

    def test_zero_matrix(self):
        for [test_matrix, expected] in self.data:
            actual = zero_matrix(test_matrix)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
