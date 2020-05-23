#!/usr/bin/python3
"""
an addition function: add_integer():
>>> add_integer(1, 1)
2
"""


def add_integer(a, b=98):
    """
    Returns the addition of a + b
    """
    if a or (type(a) is not int and type(a) is not float):
        raise TypeError('a must be an integer')
    elif type(b) is not int and type(b) is not float:
        raise TypeError('b must be an integer')
    else:
        return int(a) + int(b)
