#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list is not None:
        n = my_list[:]
        if idx < 0 or len(my_list) < idx:
            return n
            n[idx] = element
        return n
