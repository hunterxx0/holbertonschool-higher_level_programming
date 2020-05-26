#!/usr/bin/python3
"""
a LockedClass


"""

class LockedClass:
    """
    Defining the LockedClass
    """
    __slots__ = ['first_name']

    def __init__(self, first_name=""):
        self.first_name = first_name
