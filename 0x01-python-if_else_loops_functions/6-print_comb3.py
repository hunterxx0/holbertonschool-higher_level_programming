#!/usr/bin/python3
for a in range(0, 90):
    if a == 89:
        print("{:d}".format(a))
    else:
        y = a % 10
        z = a // 10
        if y > z:
            print("{:0>2d}".format(a), end=", ")
