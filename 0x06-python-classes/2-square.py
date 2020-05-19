#!/usr/bin/python3
"""a class Square that manages: size
"""


class Square:
    """a class Square with size management
    """
    def __init__(self, size=0):
        if isinstance(size, int):
            if size < 0:
                raise TypeError('size must be >= 0')
            else:
                self.__size = size
        else:
            raise TypeError('size must be an integer')
