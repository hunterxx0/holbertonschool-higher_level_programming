#!/usr/bin/python3
"""
a Rectangle Class:


"""


class Rectangle:
    """
    Defining the Rectangle class
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__height + self.__width) * 2

    def __str__(self):
        ss = ""
        if self.__height == 0 or self.__width == 0:
            return ss[:-1]
        for x in range(self.__height):
            for y in range(self.__width):
                ss += "#"
            ss += "\n"
        return ss[:-1]

    def __repr__(self):
        return "Rectangle(" + str(self.__width) + ", " + str(self.__height) +\
            ")"
