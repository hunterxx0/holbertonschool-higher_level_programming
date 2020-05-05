#!/usr/bin/python3
def add_tuple(a=(), b=()):
    if len(a) == 1:
        i = a[0]
        j = 0
    elif len(a) == 0:
        i = 0
        j = 0
    else:
        i = a[0]
        j = a[1]
    if len(b) == 1:
        k = b[0]
        l = 0
    elif len(b) == 0:
        k = 0
        l = 0
    else:
        k = b[0]
        l = b[1]
    n = (i + k, j + l)
    return n
