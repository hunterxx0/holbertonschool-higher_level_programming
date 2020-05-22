#!/usr/bin/python3
"""
an matrix dividing function: matrix_divided():
>>> matrix_divided(m, 1)
m
"""


def matrix_divided(matrix, div):
    """
    Returns a divided matrix
    """
    if not matrix:
        raise TypeError('matrix must be a matrix \
(list of lists) of integers/floats')
    k = len(matrix[0])
    if type(div) is not int and type(div) is not float:
        raise TypeError('div must be a number')
    elif div == 0:
        raise ZeroDivisionError('division by zero')
    else:
        for x in matrix:
            if not x:
                raise TypeError('Each row of the \
matrix must have the same size')
            if len(x) != k:
                raise TypeError('Each row of the \
matrix must have the same size')
            if type(x) is not list:
                raise TypeError('matrix must be a matrix \
(list of lists) of integers/floats')
            else:
                for y in x:
                    if type(y) is not int and type(y) is not float:
                        raise TypeError('matrix must be a matrix \
(list of lists) of integers/floats')
        return [[float('%.2f' % (y / div)) for y in x] for x in matrix]
