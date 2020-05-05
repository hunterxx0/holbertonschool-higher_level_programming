#!/usr/bin/python3
def multiple_returns(s):
    if len(s) == 0:
        return 0, None
    return len(s), s[0]
