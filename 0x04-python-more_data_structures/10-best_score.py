#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    s = ""
    for key in a_dictionary.keys():
        if len(s) == 0:
            s = key
        if a_dictionary[key] > a_dictionary[s]:
            s = key
    if a_dictionary[s] is None:
        return None
    return s
