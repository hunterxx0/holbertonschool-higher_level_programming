#!/usr/bin/python3
"""
salme class function: is_same_class()
>>> is_kind_of_class(1, object)
True
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if the obj is an instance of a_class
    """
    return isinstance(obj, a_class)
