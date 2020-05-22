#!/usr/bin/python3
"""
a square printing function: print_square()::
>>> def print_square(1):
#
"""


def print_square(size):
    """
    Prints a square of size 'size'
    """
    if type(size) is not int:
        raise TypeError('size must be an integer')
    elif size < 0:
        raise ValueError('size must be >= 0')
    else:
        for x in range(size):
            for y in range(size):
                print("#", end="")
            print()
