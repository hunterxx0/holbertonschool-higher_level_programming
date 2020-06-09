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

    @staticmethod
    def from_json_string(json_string):
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        ll = []
        x = ""
        c = 0
        for i in str(type(list_objs[0])):
            if c > 0 and i == "'":
                break
            if c == 2:
                x += i
            if i == '.':
                c += 1

        x += ".json"

        with open(x, mode='w', encoding='utf-8') as f:
            if list_objs:
                for z in list_objs:
                    ll.append(z.to_dictionary())
            f.write(cls.to_json_string(ll))

    @classmethod
    def create(cls, **dictionary):
        z = cls(1, 1, 1)
        z.update(**dictionary)
        return z
