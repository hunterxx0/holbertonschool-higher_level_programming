#!/usr/bin/python3
def mul(x, y):
    if x is None:
        x = 0
    if y is None:
        y = 0
    return x * y


def weight_average(m=[]):
    if m is None:
        return 0
    s, z = 0, 0
    for x, y in m:
        a, b = x, y
        if x is None:
            a = 0
        if y is None:
            b = 0
        s += mul(a, b)
        z += b
    return s / z
