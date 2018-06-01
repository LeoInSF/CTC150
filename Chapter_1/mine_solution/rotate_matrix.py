import unittest


'''
[
[1, 2, 3, 4],
[5, 6, 7, 8],
[9, 10, 11, 12],
[13, 14, 15, 16]
]

To:

[
[13, 9, 5, 1],
[14, 10, 6, 2],
[15, 11, 7, 3],
[16, 12, 8, 4]
]

'''
def rotate_matrix(matrix):

    rows = len(matrix)

    layers = rows / 2

    for layer in range(layers):

        for i in range(layer, rows - layer - 1):

            top = matrix[layer][i]

            # left -> top
            matrix[layer][i] = matrix[-i - 1][layer]

            # bottom -> left
            matrix[-i - 1][layer] = matrix[-layer - 1][-i - 1]
            # right -> bottom
            matrix[-layer -1][-i - 1]  = matrix[i][-layer - 1]
            # top -> right
            matrix[i][-layer - 1] = top

    return matrix

class Test(unittest.TestCase):
    input_data = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]

    expected_data = [
        [13, 9, 5, 1],
        [14, 10, 6, 2],
        [15, 11, 7, 3],
        [16, 12, 8, 4]
    ]

    def test_rotate_matrix(self):

        self.assertEqual(rotate_matrix(self.input_data), self.expected_data)


if __name__  == "__main__":
    unittest.main()
