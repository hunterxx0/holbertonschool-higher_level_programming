#!/usr/bin/python3
"""
Base class


"""


class Base:
    """
    Base class
    """
    __nb_objects = 0
    def __init__(self, id=None):
        if not id:
            Base.__nb_objects += 1
            id = Base.__nb_objects
        self.id = id
