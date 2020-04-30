#!/usr/bin/python3
def magic_calculation(a, b):
    from sys import argv, exit
    from magic_calculation_102 import add, sub
    if b > a:
        c = add(b, a)
        for i in range(4, 6):
            c = add(i, c)
        return c
    else:
        return sub(a, b)
