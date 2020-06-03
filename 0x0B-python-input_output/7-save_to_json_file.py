#!/usr/bin/python3
"""
Writes a JSON repr in a file function: save_to_json_file()
>>> save_to_json_file(obj, "text")
1 line
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes a JSON repr in the file
    """
    with open(filename, mode='w', encoding='utf-8') as f:
        f.write(json.dumps(my_obj))
