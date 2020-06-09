#!/usr/bin/python3
"""
Base class


"""
import csv
import json
from os import path


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
        if not list_dictionaries or len(list_dictionaries) == 0:
            return ('"[]"')

        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        ll = []
        x = cls.__name__ + '.json'

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

    @classmethod
    def load_from_file(cls):
        if not path.exists(cls.__name__ + '.json'):
            return []
        x = cls.__name__ + '.json'

        with open(x, encoding='utf-8') as f:
            ll = []
            dt = cls.from_json_string(f.read())
            for a in dt:
                ll.append(cls.create(**a))
            return ll

    @classmethod
    def save_to_file_csv(cls, list_objs):
        x = cls.__name__ + '.csv'
        with open(x, mode='w', encoding='utf-8') as f:
            if list_objs:
                w = csv.writer(f)
                for z in list_objs:
                    ll = []
                    ll.append(z.to_dictionary()['id'])
                    if 'height' in z.to_dictionary():
                        ll.append(z.to_dictionary()['width'])
                        ll.append(z.to_dictionary()['height'])
                    else:
                        ll.append(z.to_dictionary()['size'])
                    ll.append(z.to_dictionary()['x'])
                    ll.append(z.to_dictionary()['y'])
                    w.writerow(ll)

    @classmethod
    def load_from_file_csv(cls):
        if not path.exists(cls.__name__ + '.csv'):
            return []
        x = cls.__name__ + '.csv'
        with open(x, encoding='utf-8') as f:
            r = csv.reader(f)
            ll = []
            for s in r:
                dt = {}
                dt['id'] = int(s[0])
                if len(s) == 5:
                    dt['width'] = int(s[1])
                    dt['height'] = int(s[2])
                else:
                    dt['size'] = int(s[1])
                dt['x'] = int(s[-2])
                dt['y'] = int(s[-1])
                ll.append(dt)
            zz = []
            for a in ll:
                zz.append(cls.create(**a))
            return zz
