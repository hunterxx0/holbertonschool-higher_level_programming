#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is not None:
        m = []
        i = 0
        ls = []
        for i in range(len(matrix[i])):
            ls = [x**2 for x in matrix[i]]
            m.append(ls)
        return m
