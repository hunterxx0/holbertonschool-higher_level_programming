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

    def area(self):
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if isinstance(size, int):
            if size < 0:
                raise TypeError('size must be >= 0')
            else:
                self.__size = size
        else:
            raise TypeError('size must be an integer')
