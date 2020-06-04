#!/usr/bin/python3
"""
Empty class: BaseGeometry


"""


class BaseGeometry:
    """
    BaseGeometry class
    """
    def area(self):
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(str(name) + ' must be an integer')
        if value <= 0:
            raise ValueError(str(name) + ' must be greater than 0')


class Rectangle(BaseGeometry):
    """
    Rectangle class
    """
    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)

    def area(self):
        return self.__height * self.__width


class Square(Rectangle):
    """
    Square class
    """
    def __init__(self, size):
        super().integer_validator("size", size)
        super().__init__(size, size)
