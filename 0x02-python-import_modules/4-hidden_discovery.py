#!/usr/bin/python3
import hidden_4
lis = dir(hidden_4)
new = []
for a in lis:
    if a[0] != '_':
        new.append(a)
new.sort()
for a in new:
    print(a)
