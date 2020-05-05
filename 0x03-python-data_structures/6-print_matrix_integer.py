#!/usr/bin/python3
def print_matrix_integer(m=[[]]):
    y = len(m[0])
    if y == 0:
        print()
        return
    x = len(m)
    for i in range(0, x):
        for j in range(0, y):
            if j != y - 1:
                print("{}".format(m[i][j]), end=' ')
            else:
                print("{}".format(m[i][j]))
