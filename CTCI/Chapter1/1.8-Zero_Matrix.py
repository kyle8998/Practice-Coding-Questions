# CTCI 1.8
# Zero Matrix

import unittest

# My Solution

def zero_matrix(matrix):
    zero_row = []
    zero_col = []

    # Mark each row and column for zeroing
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                zero_row.append(i)
                zero_col.append(j)

    # Zero rows
    for row in zero_row:
        for n in range(len(matrix[row])):
            matrix[row][n] = 0

    # Zero cols
    for col in zero_col:
        for m in range(len(matrix)):
            matrix[m][col] = 0

    return matrix


#-------------------------------------------------------------------------------
# CTCI Solution

def zero_matrix2(matrix):
    m = len(matrix)
    n = len(matrix[0])
    rows = []
    cols = []

    for x in range(m):
        for y in range(n):
            if matrix[x][y] == 0:
                rows.append(x)
                cols.append(y)

    for row in rows:
        nullify_row(matrix, row)

    for col in cols:
        nullify_col(matrix, col)

    return matrix


def nullify_row(matrix, row):
    for i in range(len(matrix[0])):
        matrix[row][i] = 0


def nullify_col(matrix, col):
    for i in range(len(matrix)):
        matrix[i][col] = 0

#-------------------------------------------------------------------------------
#Testing

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
