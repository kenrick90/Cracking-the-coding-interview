import unittest


def zero_Matrix(matrix):
    firstRowHasZero = False
    firstColumnHasZero = False

    rowNum = len(matrix)
    columnNum = len(matrix[0])

    for i in range(rowNum):
        if matrix[i][0] == 0:
            firstColumnHasZero = True

    for i in range(columnNum):
        if matrix[0][i] == 0:
            firstRowHasZero = True

    for i in range(1, rowNum):
        for j in range(1, columnNum):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    for i in range(1, rowNum):
        if matrix[i][0] == 0:
            nullifyRow(matrix, i)

    for i in range(1, columnNum):
        if matrix[0][i] == 0:
            nullifyCol(matrix, i)

    if firstRowHasZero is True:
        nullifyRow(matrix, 0)

    if firstColumnHasZero is True:
        nullifyCol(matrix, 0)

    return matrix


def nullifyRow(matrix, row):
    columnNum = len(matrix[0])
    for i in range(columnNum):
        matrix[row][i] = 0


def nullifyCol(matrix, col):
    rowNum = len(matrix)
    for i in range(rowNum):
        matrix[i][col] = 0


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
            actual = zero_Matrix(test_matrix)
            self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()

