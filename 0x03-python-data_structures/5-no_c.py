#!/usr/bin/python3
def no_c(s):
    n = ""
    for i in s:
        if i != 'c' and i != 'C':
            n += i
    return n
