#!/usr/bin/python3
def delete_at(m=[], i=0):
    if i < 0 or len(m) - 1 < i:
        return m
    del m[i]
    return m
