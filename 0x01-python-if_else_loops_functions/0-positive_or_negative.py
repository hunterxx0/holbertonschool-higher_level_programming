#!/usr/bin/python3
import random
n = random.randint(-10, 10)
if n == 0:
    print("{} is zero".format(n))
elif n < 0:
    print("{} is negative".format(n))
else:
    print("{} is positive".format(n))
