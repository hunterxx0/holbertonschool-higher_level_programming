#!/usr/bin/python3
""" finds a peak in a list of unsorted integers. """


def find_peak(list_of_integers):
    """ finds a peak in a list of unsorted integers. """
    if not list_of_integers:
        return None
    else:
        l_arr = len(list_of_integers)
        lo = 0
        hi = l_arr - 1
        while(lo <= hi):
            if lo == hi:
                return list_of_integers[lo]
            mid = int(lo + (hi - lo) / 2)
            if list_of_integers[mid] < list_of_integers[mid + 1]:
                lo = mid + 1
            else:
                hi = mid
        return None
