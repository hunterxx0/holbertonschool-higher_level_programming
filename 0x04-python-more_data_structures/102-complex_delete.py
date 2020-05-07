#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    s = []
    for key in a_dictionary.keys():
        if a_dictionary[key] == value:
            s.append(key)
    for key in s:
        del a_dictionary[key]
    return a_dictionary
