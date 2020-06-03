#!/usr/bin/python3
"""
Returns an obj from the JSON representation function: from_json_string()
>>> from_json_string(obj)
...
"""
import json


def from_json_string(my_str):
    """
    Returns and obj from the JSON representation
    """
    return json.loads(my_str)
