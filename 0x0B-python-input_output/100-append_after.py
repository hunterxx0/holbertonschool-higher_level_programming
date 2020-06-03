#!/usr/bin/python3
"""
Writes a text in a file function: write_file()
>>> write_file("a.txt", "text")
1 line
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Writes a text in the file
    """
    with open(filename, mode='r', encoding='utf-8') as f:
        ll = f.readlines()

    with open(filename, mode='w', encoding='utf-8') as f:
        for l in ll:
            f.write(l)
            if search_string in l:
                f.write(new_string)
