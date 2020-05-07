#!/usr/bin/python3
def mul(x, y):
    if x == None:
        x = 0
    if y == None:
        y = 0
    return x * y


def weight_average(m=[]):
    if m is None:
        return 0
    s, z = 0, 0
    for x, y in m:
        if x == None:
            x = 0
        if y == None:
            y = 0
        s += mul(x, y)
        z += y
    return s / z
