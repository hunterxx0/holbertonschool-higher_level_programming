#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is not None:
        y = len(matrix[0])
        if y == 0:
            print()
            return
        x = len(matrix)
        for i in range(0, x):
            for j in range(0, y):
                if j != y - 1:
                    print("{}".format(matrix[i][j]), end=' ')
                else:
                    print("{}".format(matrix[i][j]))
