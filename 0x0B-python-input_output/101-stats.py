#!/usr/bin/python3
"""
Writes a text in a file function: write_file()
>>> write_file("a.txt", "text")
1 line
"""
import sys


def append_after(filename="", search_string="", new_string=""):
    """
    Writes a text in the file
    """
    data = sys.stdin.readlines()
    print(len(data))

#    dt = {'200': 0, '301': 0, '400': 0, '403': 0, '404': 0, '405': 0, '500': 0#}
#    with open(sys.stdin, mode='r', encoding='utf-8') as f:
#        ll = f.readlines()
#        for l in ll:
#            ss = l.split(' ')
#            print[ss[6]]
