#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) != str:
        return 0
    if "MMMM" in roman_string:
        return 0
    s = 0
    o = 0
    c = ''
    a = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for i in range(0, len(roman_string)):
        if roman_string[i] not in a.keys():
            return 0
        if roman_string[i] == 'I' and i + 1 < len(roman_string):
            if roman_string[i + 1] != 'I':
                o = 1
        if roman_string[i] == 'C' and i + 1 < len(roman_string):
            if roman_string[i + 1] == 'M' or roman_string[i + 1] == 'D':
                o = 100
        if roman_string[i] == 'X' and i + 1 < len(roman_string):
            c = roman_string[i + 1]
            if c == 'C' or c == 'L':
                o = 10
        if o != 0:
            s += a[roman_string[i]] - o
        else:
            s += a[roman_string[i]]
    return s
