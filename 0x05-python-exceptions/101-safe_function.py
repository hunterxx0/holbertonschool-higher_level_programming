#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        x = fct(*args)
        return x
    except Exception as ex:
        print("Exception: {}".format(ex), file=sys.stderr)
