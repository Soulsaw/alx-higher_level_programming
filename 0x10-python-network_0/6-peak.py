#!/usr/bin/python3
"""This function is to finds the peak in the list of integers
"""


def find_peak(list_of_integers):
    """find the peak elements of the lists
    """
    max = None
    for ele in list_of_integers:
        if max is None or max < ele:
            max = ele
    return max
