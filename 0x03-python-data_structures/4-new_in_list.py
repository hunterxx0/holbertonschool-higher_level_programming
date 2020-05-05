#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    n = my_list[:]
    if idx < 0 or len(my_list) - 1 < idx:
        return n
    n[idx] = element
    return n
