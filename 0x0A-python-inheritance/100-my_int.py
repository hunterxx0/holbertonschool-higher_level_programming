#!/usr/bin/python3
"""
MyInt class: int


"""


class MyInt(int):
    """
    BaseGeometry class
    """
    def __eq__(self, other):
        return(self.numerator != other.numerator)

    def __ne__(self, other):
        return(self.numerator == other.numerator)
