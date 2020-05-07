#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string == None or type(roman_string) != str:
        return 0
    s = 0
    o = 0
    a = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for i in range(0, len(roman_string)):
        if roman_string[i] not in a.keys():
            return 0
        if roman_string[i] == 'I' and i + 1 < len(roman_string):
            if roman_string[i + 1] != 'I':
                o = 1
        if o != 0:
            s += a[roman_string[i]] - o
        else:
            s += a[roman_string[i]]
    return s
