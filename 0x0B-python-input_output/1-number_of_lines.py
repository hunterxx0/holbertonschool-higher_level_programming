#!/usr/bin/python3
"""
Number of lines in a file function: number_of_lines()
>>> number_of_lines("a.txt")
1
"""


def number_of_lines(filename=""):
    """
    Returns the number of lines in the file
    """
    x = 0
    with open(filename, encoding='utf-8') as f:
        for l in f:
            x += 1
    return x
