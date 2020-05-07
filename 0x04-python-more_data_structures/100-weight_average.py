#!/usr/bin/python3
def weight_average(m=[]):
    if not m:
        return 0
    s = 0
    z = 0
    for x, y in m:
        s += x * y
        z += y
    return s / z
