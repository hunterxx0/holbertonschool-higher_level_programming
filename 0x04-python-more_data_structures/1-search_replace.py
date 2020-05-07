#!/usr/bin/python3
def search_replace(my_list, search, replace):
    m = []
    z = 0
    for x in my_list:
        if x == search:
            z = replace
        else:
            z = x
        m.append(z)
    return m
