#!/usr/bin/python3
"""
MyList class: print_sorted()
>>> my_list.print_sorted()
[1, 2, 3, 4, 5]
"""


class MyList(list):
    """
    print_sorted()
    """
    def print_sorted(self):
        """
        print_sorted()
        """
        ll = list(self)
        ll.sort()
        print(ll)
