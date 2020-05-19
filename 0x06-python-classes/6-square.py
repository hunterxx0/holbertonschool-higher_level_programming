#!/usr/bin/python3
"""a class Square that manages: size
"""


class Square:
    """a class Square with size management
    """
    def __init__(self, size=0, position=(0, 0)):
        if isinstance(size, int):
            if size < 0:
                raise TypeError('size must be >= 0')
            else:
                self.__size = size
        else:
            raise TypeError('size must be an integer')
        if len(position) != 2 or not isinstance(position[0], int)\
           or not isinstance(position[1], int) or position[1] < 0\
           or position[0] < 0 or not isinstance(position, tuple):
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = position

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.size == 0:
            print()
        for i in range(self.position[1]):
            print()
        for x in range(self.size):
            for y in range(self.size + self.position[0]):
                if y < self.position[0]:
                    print(' ', end='')
                else:
                    print('#', end='')
            print()

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        if len(position) != 2 or not isinstance(position[0], int)\
           or not isinstance(position[1], int) or position[1] < 0\
           or position[0] < 0 or not isinstance(position, tuple):
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = position

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
