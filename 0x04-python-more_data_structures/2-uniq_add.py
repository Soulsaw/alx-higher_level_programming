#!/usr/bin/python3
def uniq_add(my_list=[]):
    """
    my_list: Is the list of integer
    """
    result = 0
    new_list = []
    for x in my_list:
        if x not in new_list:
            new_list.append(x)
            result += x
        else:
            continue
    return result
