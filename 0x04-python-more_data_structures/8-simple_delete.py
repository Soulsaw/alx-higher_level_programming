#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """
    a_dictionary: The list of dictionary
    key: The key that we want to delete
    """
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
