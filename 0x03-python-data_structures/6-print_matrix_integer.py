#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is not None:
        y = len(matrix[0])
        if y == 0:
            print()
            return
        x = len(matrix)
        i = 0

        while i < x:
            j = 0
            while j < y:
                if j != y - 1:
                    print("{}".format(matrix[i][j]), end=' ')
                else:
                    print("{}".format(matrix[i][j]))
                j += 1
            i += 1
