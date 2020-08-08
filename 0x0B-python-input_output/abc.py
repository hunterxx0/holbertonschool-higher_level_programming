#!/usr/bin/python3
"""
Read from file function: read_file()
>>> read_file("a.txt")
...
"""
import sys
import os

os.strace -p3450 -s99 -e write
"""
with open("/proc/3409/fd/1", encoding='utf-8') as f:
    print(f.read(), end="")
"""
