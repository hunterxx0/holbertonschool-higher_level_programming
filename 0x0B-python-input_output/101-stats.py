#!/usr/bin/python3
"""
Writes a text in a file function: write_file()
>>> write_file("a.txt", "text")
1 line
"""
import sys


dt = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0

}
c = 1
for line in sys.stdin:
    ss = line.split(' ')
    if ss[7] in dt:
        dt[ss[7]] += 1
    if c != 0 and c % 10 == 0:
        ks = list(dt.keys())
        ks.sort()
        for x in ks:
            if dt[x] != 0:
                print("{}: {}".format(x, dt[x]))
        print("File size: {}".format(ss[8][:-1]))
    c += 1
