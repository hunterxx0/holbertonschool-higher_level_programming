#!/usr/bin/python3
"""
Writes a text in a file function: write_file()
>>> write_file("a.txt", "text")
1 line
"""


def write_file(filename="", text=""):
    """
    Writes a text in the file
    """
    with open(filename, mode='w', encoding='utf-8') as f:
        c = f.write(text)
        return c
