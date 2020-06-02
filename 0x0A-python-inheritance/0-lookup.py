#!/usr/bin/python3
"""
lookup function: lookup()
>>> lookup(class)
[...]
"""


def lookup(obj):
    """
    Returns a list of available attributes and methods
    """
    return [x for x in dir(obj)]
