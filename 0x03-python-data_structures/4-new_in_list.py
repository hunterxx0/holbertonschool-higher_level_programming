#!/usr/bin/python3
def new_in_list(m, i, e):
    n = m[:]
    if i < 0 or len(m) < i:
        return n
    n[i] = e
    return n
