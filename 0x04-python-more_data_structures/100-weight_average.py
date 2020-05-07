#!/usr/bin/python3
def weight_average(m=[]):
    if m is None:
        return 0
    mul = lambda x, y: x * y
    s, z = 0, 0
    for x in m:
       s += mul(x[0], x[1])
       z += x[1]
    s /= z
    return s
