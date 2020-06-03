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

    def to_json(self):
        """
        to json funct
        """
        return self.__dict__
