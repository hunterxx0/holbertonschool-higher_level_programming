#!/usr/bin/python3
def magic_string(m=[-1]):
    m[0] += 1
    return ("holberton, " * (m[0]) + ("holberton" * (m[0] - (m[0] - 1))))
