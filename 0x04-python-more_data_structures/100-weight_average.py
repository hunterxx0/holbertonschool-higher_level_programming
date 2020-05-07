#!/usr/bin/python3
def mul(x, y):
    return x * y


def weight_average(m=[]):
    if m is None:
        return 0
    s, z = 0, 0
    for x, y in m:
        s += mul(x, y)
        z += y
    return s / z
