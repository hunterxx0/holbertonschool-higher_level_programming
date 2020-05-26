#!/usr/bin/python3
def magic_string(m=[-1]):
    m[0] += 1
    return ("Holberton, " * (m[0]) + ("Holberton" * (m[0] - (m[0] - 1))))
