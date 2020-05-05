#!/usr/bin/python3
def print_reversed_list_integer(m=[]):
    for i in range(len(m)-1, -1, -1):
        print("{}".format(m[i]))
