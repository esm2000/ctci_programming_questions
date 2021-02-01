# Write an algorithm such that if an element
# in an MxN matrix is 0, its entire row and
# column are set to 0.


def zeroMatrix(matrix):

    # to keep track of what rows and
    # columns need to be nullified
    rows = set()
    columns = set()

    # matrix dimensions
    nrows = len(matrix)
    ncols = len(matrix[0])

    for i in range(nrows):
        for j in range(ncols):
            if matrix[i][j] == 0:
                rows.add(i)
                columns.add(j)

    for row in rows:
        for i in range(ncols):
            matrix[row][i] = 0

    for col in columns:
        for i in range(nrows):
            matrix[i][col] = 0


a = [[1, 2, 3, 0], [5, 0, 7, 8], [9, 10, 11, 12]]

print('ORIGINAL MATRIX')
for row in a:
    print(row)

zeroMatrix(a)

print('ALTERED MATRIX')
for row in a:
    print(row)
