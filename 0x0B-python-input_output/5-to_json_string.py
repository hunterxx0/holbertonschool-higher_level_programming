#!/usr/bin/python3
"""
Returns the JSON representation function: to_json_string()
>>> to_json_string(obj)
...
"""
import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string)
    """
    return json.dumps(my_obj)
