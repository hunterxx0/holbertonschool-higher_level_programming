#!/usr/bin/python3
"""
Empty class: BaseGeometry


"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class
    """
    def __init__(self, size):
        super().integer_validator("size", size)
        super().__init__(size, size)
