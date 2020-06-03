#!/usr/bin/python3
"""
adds all arguments to a Python list, and then save them to a file


"""


class Student:
    """
    Student Class
    """
    def __init__(self, first_name, last_name, age):
        """
        init funct
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        to json funct
        """
        if not attrs or type(attrs) is not list:
            return self.__dict__
        dt = {}
        for x in attrs:
            if type(x) is not str:
                return self.__dict__
            if x in self.__dict__:
                dt[x] = self.__dict__[x]
        if len(dt) == len(self.__dict__):
            return self.__dict__
        else:
            return dt
