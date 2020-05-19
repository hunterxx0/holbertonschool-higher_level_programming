#!/usr/bin/python3
"""a class MagicClass takes radius
"""
import math


class MagicClass:
    """a class MagicClass takes and int or flaot radius
    """
    def __init__(self, radius=0):
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        else:
            self.__radius = radius

    def area(self):
        return self.__radius ** 2 * math.pi

    def circumference(self):
        return 2 * math.pi * self.__radius
