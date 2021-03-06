#!/usr/bin/python3
"""a class Square that manages: size
"""


class Square:
    """a class Square with size management
    """
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    def __str__(self):
        ss = ""
        if self.size == 0:
            ss += "\n"
        else:
            for i in range(self.__position[1]):
                ss += "\n"
            for x in range(self.__size):
                for y in range(self.__position[0]):
                    ss += " "
                for y in range(self.__size):
                    ss += "#"
                ss += "\n"
        return ss[:-1]

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2\
           or not isinstance(value[0], int) or value[0] < 0\
           or not isinstance(value[1], int) or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = value

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            if value < 0:
                raise TypeError('size must be >= 0')
            else:
                self.__size = value
        else:
            raise TypeError('size must be an integer')

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for x in range(self.__size):
                for y in range(self.__position[0]):
                    print(' ', end='')
                for y in range(self.__size):
                    print('#', end='')
                print()
