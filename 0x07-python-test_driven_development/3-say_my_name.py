#!/usr/bin/python3
"""
an name function: say_my_name():
>>> say_my_name("Mhamed", "Azouzi")
My name is Mhamed Azouzi
"""


def say_my_name(first_name, last_name=""):
    """
    Prints My name is first_name last_name
    """
    if not first_name or type(first_name) is not str:
        raise TypeError('first_name must be a string')
    elif type(last_name) is not str:
        raise TypeError('last_name must be a string')
    else:
        print("My name is {} {}".format(first_name, last_name))
