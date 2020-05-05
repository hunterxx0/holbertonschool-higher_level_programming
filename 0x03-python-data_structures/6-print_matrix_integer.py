#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    i = 0
    while i < len(matrix):
        j = 0
        while j < len(matrix[0]):
            if j != len(matrix[0]) - 1:
                print("{:d}".format(matrix[i][j]), end=' ')
            else:
                print("{:d}".format(matrix[i][j]))
            j += 1
        i += 1
    if len(matrix[0]) == 0:
        print()
