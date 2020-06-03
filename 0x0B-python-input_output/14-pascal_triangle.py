#!/usr/bin/python3
"""
adds all arguments to a Python list, and then save them to a file


"""


def pascal_triangle(n):
    """
    Triangle
    """
    if n <= 0:
        return []
    ll = [[0 for x in range(n)] for y in range(n)]
    for i in range(n):
        for x in range(i + 1):
            if x == 0 or x == i:
                ll[i][x] = 1
            else:
                ll[i][x] = ll[i - 1][x - 1] + ll[i - 1][x]
    zz = []
    for x in range(len(ll) - 1, -1, -1):
        for i in range(len(ll[x]) - 1, -1, -1):
            if ll[x][i] == 0:
                zz.append(x)
                zz.append(i)
    x = 0
    while x < len(zz):
        if x == 0 or x % 2 == 0:
            del ll[zz[x]][zz[x + 1]]
        x += 1
    return ll
