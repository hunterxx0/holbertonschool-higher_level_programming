#!/usr/bin/python3
"""
Writes a JSON repr in a file function: load_from_json_file()
>>> load_from_json_file(obj, "text")
1 line
"""
import json


def load_from_json_file(filename):
    """
    Writes a JSON repr in the file
    """
    with open(filename, encoding='utf-8') as f:
        return json.loads(f.read())
