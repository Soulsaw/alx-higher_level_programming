#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """
    my_list: It's content the list of integers
    """
    new_list = []
    for val in my_list:
        if int(val) % 2 == 0:
            new_list.append(True)
        else:
            new_list.append(False)
    return new_list
