#!/usr/bin/python3
"""
A matrix mul function: matrix_mul():
>>> matrix_mul([[1, 2]], [[3, 4], [5, 6]]):
[[13, 16]]
"""


def matrix_mul(m_a, m_b):
    """
    Mul a Matrix
    """
    if type(m_a) is not list:
        raise TypeError('m_a must be a list')
    if type(m_b) is not list:
        raise TypeError('m_b must be a list')
    for x in m_a:
        if type(x) is not list:
            raise TypeError('m_a must be a list of lists')
    for y in m_b:
        if type(y) is not list:
            raise TypeError('m_b must be a list of lists')
    if m_a is None or any(x is None for x in m_a):
        raise ValueError("m_a can't be empty")
    if m_b is None or any(y is None for y in m_b):
        raise ValueError("m_b can't be empty")
    for x in m_a:
        for y in x:
            if type(y) is not int and type(y) is not float:
                raise TypeError('m_a should contain only integers or floats')
    for x in m_b:
        for y in x:
            if type(y) is not int and type(y) is not float:
                raise TypeError('m_b should contain only integers or floats')
    y = len(m_a[0])
    for x in m_a:
        if len(x) != y:
            raise TypeError('each row of m_a must be of the same size')
    y = len(m_b[0])
    for x in m_b:
        if len(x) != y:
            raise TypeError('each row of m_b must be of the same size')
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    return[[sum(a * b for a, b in zip(x, y)) for y in zip(*m_b)] for x in m_a]
