#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """
    my_list: Is the list of variables such as integer, string, object

    """
    if my_list is None:
        return
    my_list.reverse()
    for item in my_list:
        print("{:d}".format(item))
