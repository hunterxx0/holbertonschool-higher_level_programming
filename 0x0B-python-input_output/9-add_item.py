#!/usr/bin/python3
"""
adds all arguments to a Python list, and then save them to a file


"""
from os import path
import json
from sys import argv
loadf = __import__('8-load_from_json_file').load_from_json_file
savef = __import__('7-save_to_json_file').save_to_json_file

if path.exists('add_item.json'):
    l = loadf('add_item.json')
else:
    l = []
if len(argv) > 1:
    for c in range(1, len(argv)):
        l.append(argv[c])
savef(l, 'add_item.json')
