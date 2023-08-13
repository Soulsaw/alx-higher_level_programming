#!/usr/bin/python3
def element_at(my_list, idx):
    """
    my_list: Is the list of elements
    idx: Is the index of the retrieve element
    """
    if idx < 0 or idx >= len(my_list):
        return "None"
    else:
        return my_list[idx]
