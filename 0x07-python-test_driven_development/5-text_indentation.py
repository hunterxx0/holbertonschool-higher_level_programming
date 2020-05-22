#!/usr/bin/python3
"""
a text printing function: text_indentation():
>>> text_indentation(hello.       world):
hello.\n\nworld
"""


def text_indentation(text):
    """
    Prints the text without indentations
    """
    if type(text) is not str:
        raise TypeError('text must be a string')
    else:
        pp = ":.?"
        x = 0
        while text[x] == ' ':
            x += 1
        while x < len(text):
            print("{}".format(text[x]), end="")
            if text[x] in pp:
                print('\n')
                z = 0
                while text[x + 1] == " ":
                    x += 1
            x += 1
