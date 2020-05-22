#!/usr/bin/python3
"""
A matrix mul function with Numpy: matrix_mul():
>>> matrix_mul([[1, 2]], [[3, 4], [5, 6]]):
[[13, 16]]
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Mul a Matrix using Numpy
    """
    return np.matmul(m_a, m_b)
