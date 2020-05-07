#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    nd = {}
    for key in a_dictionary.keys():
        nd[key] = a_dictionary[key] * 2
    return nd
