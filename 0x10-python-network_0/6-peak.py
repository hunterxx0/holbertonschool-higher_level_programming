#!/usr/bin/python3
""" finds a peak in a list of unsorted integers. """


def f_peak(arr, low, high, n):
    mid = low + (high - low)/2
    mid = int(mid)
    if ((mid == 0 or arr[mid - 1] <= arr[mid]) and
        (mid == n - 1 or arr[mid + 1] <= arr[mid])):
        return mid
    elif (mid > 0 and arr[mid - 1] > arr[mid]):
        return f_peak(arr, low, (mid - 1), n)
    else:
        return f_peak(arr, (mid + 1), high, n)

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



        #return (f_peak(list_of_integers, 0, l_arr - 1, l_arr))
