#!/usr/bin/python3
import random
n = random.randint(-10, 10)
if n == 0:
    print("{:d} is zero".format(n))
elif n < 0:
    print("{:d} is negative".format(n))
else:
    print("{:d} is positive".format(n))
