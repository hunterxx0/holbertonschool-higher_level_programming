#!/usr/bin/python3
"""
adds all arguments to a Python list, and then save them to a file


"""
import json


def class_to_json(obj):
    return obj.__dict__
