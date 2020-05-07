#!/usr/bin/python3
def best_score(a_dictionary):
    s = ""
    for key in a_dictionary.keys():
        if len(s) == 0:
            s = key
        if a_dictionary[key] > a_dictionary[s]:
            s = key
    return s
