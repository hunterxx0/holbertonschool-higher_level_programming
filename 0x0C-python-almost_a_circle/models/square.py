#!/usr/bin/python3
""" Square class """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value


    def __str__(self):
        return ("[Square] ({}) {}/{} \
- {}".format(self.id, self.x, self.y, self.size))

    def update(self, *args, **kwargs):
        """ upd """
        if len(args) > 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                if i == 1:
                    self.size = args[i]
                if i == 2:
                    self.x = args[i]
                if i == 3:
                    self.y = args[i]
        if not args and kwargs:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """ dict """
        dt = {}
        dt["x"] = self.x
        dt["y"] = self.y
        dt["id"] = self.id
        dt["size"] = self.size
        return dt
