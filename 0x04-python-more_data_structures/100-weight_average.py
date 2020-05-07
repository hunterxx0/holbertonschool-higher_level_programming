#!/usr/bin/python3
def mul(x, y):
    return x * y


def weight_average(m=[]):
    if m is None:
        return 0
    s, z = 0, 0
    for x in m:
        s += mu(x[0], x[1])
        z += x[1]
    s /= z
    return s
