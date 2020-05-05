#!/usr/bin/python3
def replace_in_list(m, i, e):
    if i < 0 or len(m) < i:
        return m
    m[i] = e
    return m
