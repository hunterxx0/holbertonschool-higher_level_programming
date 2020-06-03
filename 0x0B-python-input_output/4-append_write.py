#!/usr/bin/python3
"""
Appends a text in a file function: append_write()
>>> append_write("a.txt", "text")
1 line
"""


def append_write(filename="", text=""):
    """
    Appends a text in the file
    """
    with open(filename, mode='a', encoding='utf-8') as f:
        c = f.write(text)
        return c
