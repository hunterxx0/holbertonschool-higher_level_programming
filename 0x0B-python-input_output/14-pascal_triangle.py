#!/usr/bin/python3
"""
adds all arguments to a Python list, and then save them to a file


"""


def pascal_triangle(n):
    if n <= 0:
        return ()

    ll = []
    c = 1
    for i in range(n):
        tmp = []
        if i == 0:
            tmp.append(1)
        else:
            for x in range(c):
                if c % 2 == 0:
                    if x == c / 2:
                        z = x
                        while z != 0:
                            tmp.append(tmp[z-1])
                            z -= 1
                    else:
                        h = 1
                        tmp.append(h)
                        h = c - h




        c += 1
        ll.append(tmp)
