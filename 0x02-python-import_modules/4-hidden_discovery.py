#!/usr/bin/python3
import hidden_4
l = dir(hidden_4)
n = []
for a in l:
    if a[0] != '_':
        n.append(a)
n.sort()
print(*n, sep = "\n")
