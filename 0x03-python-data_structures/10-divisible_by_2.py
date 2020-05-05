#!/usr/bin/python3
def divisible_by_2(m=[]):
    if m is not None:
        x = m[:]
        for i in m:
            if m[i] % 2 == 0:
                x[i] = True
            else:
                x[i] = False
        return x
