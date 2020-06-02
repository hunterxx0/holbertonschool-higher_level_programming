#!/usr/bin/python3
"""
Add attr function: add_attribute()
>>> add_attribute(class, attrname, value)
[...]
"""


def add_attribute(mc, att, value):
    """
    Returns a list of available attributes and methods
    """
    if "__dict__" in dir(mc):
        setattr(mc, att, value)
    else:
        raise TypeError("can't add new attribute")
