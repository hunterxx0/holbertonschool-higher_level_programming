#!/usr/bin/python3
"""
Read from file function: read_file()
>>> read_file("a.txt")
...
"""


def read_file(filename=""):
    """
    Prints the file contents
    """
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")
