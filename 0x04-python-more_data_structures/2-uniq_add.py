#!/usr/bin/python3
def uniq_add(my_list=[]):
    s = 0
    m = []
    for x in my_list:
        if x not in m:
            m.append(x)
    for z in m:
        s += z
    return s
