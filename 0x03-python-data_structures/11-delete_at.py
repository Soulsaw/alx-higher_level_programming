#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """
    my_list: Is the list of elements
    idx: Is the index of the retrieve element
    """
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        del my_list[idx]
        return my_list
