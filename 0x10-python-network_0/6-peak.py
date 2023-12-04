#!/usr/bin/python3
"""This function is to finds the peak in the list of integers
"""


def find_peak(list_of_integers):
    """find the peak elements of the lists
    """
    max = list_of_integers[0] if len(list_of_integers) > 0 else None
    for ele in list_of_integers:
        if max < ele:
            max = ele
    return max
