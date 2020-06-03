#!/usr/bin/python3
"""
Prints a number of lines in a file function: read_lines()
>>> read_lines("a.txt", 1)
1 line
"""


def read_lines(filename="", nb_lines=0):
    """
    Prints a number of lines in the file
    """
    with open(filename, encoding='utf-8') as f:
        lines = f.readlines()
        for l in range(len(lines)):
            if l == nb_lines and nb_lines != 0:
                break
            print(lines[l], end='')
