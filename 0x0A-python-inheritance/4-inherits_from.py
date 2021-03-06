#!/usr/bin/python3
"""
salme class function: is_same_class()
>>> is_same_class(1, int)
True
"""


def inherits_from(obj, a_class):
    """
    Returns True if the obj is an instance of a_class
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
