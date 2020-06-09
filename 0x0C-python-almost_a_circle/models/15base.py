#!/usr/bin/python3
"""
Base class


"""
import json


class Base:
    """
    Base class
    """
    __nb_objects = 0
    def __init__(self, id=None):
        if not id:
            Base.__nb_objects += 1
            id = Base.__nb_objects
        self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        if not list_dictionaries:
            return ('"[]"')

        return json.dumps(list_dictionaries)
