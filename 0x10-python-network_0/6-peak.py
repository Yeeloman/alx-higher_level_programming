#!/usr/bin/python
# a function that finds a peak in a list of unsorted integers.

def find_peak(list_of_integers):
    """find the peak of a list
    Args:
        list_of_integers: the list
    """
    if not list_of_integers:
        return None
    peak_index = max(enumerate(list_of_integers), key=lambda x: x[1])[0]
    peak_value = list_of_integers[peak_index]
    return peak_value
