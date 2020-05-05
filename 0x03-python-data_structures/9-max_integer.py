#!/usr/bin/python3
def max_integer(m=[]):
    if len(m) == 0:
        return None
    x = m[0]
    for i in m:
        if i > x:
            x = i
    return x
