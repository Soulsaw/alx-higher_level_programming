#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """
    my_list: Is the list of elements
    idx: Is the index of the retrieve element
    element: Is the new element to replace
    """
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        my_list[idx] = element
        return my_list
