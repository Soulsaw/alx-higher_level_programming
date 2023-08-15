#!/usr/bin/python3
def no_c(my_string):
    """
    my_string: Is the string that we want to remove all c and C

    """
    new_string = ''
    for val in my_string:
        if val not in 'cC':
            new_string += val
    return new_string
