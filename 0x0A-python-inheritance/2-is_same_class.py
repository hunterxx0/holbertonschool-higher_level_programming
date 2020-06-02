#!/usr/bin/python3
"""
salme class function: is_same_class()
>>> is_same_class(1, int)
True
"""


def is_same_class(obj, a_class):
    """
    Returns True if the obj is an instance of a_class
    """
    return type(obj) is a_class
