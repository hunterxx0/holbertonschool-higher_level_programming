#!/usr/bin/python3
def element_at(m, i):
    if i < 0 or len(m) < i:
        return None
    return m[i]
