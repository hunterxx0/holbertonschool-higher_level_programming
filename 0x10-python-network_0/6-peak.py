#!/usr/bin/python3
""" finds a peak in a list of unsorted integers. """

def find_peak(list_of_integers):
    """ finds a peak in a list of unsorted integers. """
    if not list_of_integers:
        return None
    else:
        return (max(list_of_integers))
