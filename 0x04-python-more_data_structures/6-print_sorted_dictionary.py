#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """
    a_dictionary: It's the dictionary
    """
    keys = list(a_dictionary)
    keys.sort()
    for key in keys:
        print("{}: {}".format(key, a_dictionary[key]))
