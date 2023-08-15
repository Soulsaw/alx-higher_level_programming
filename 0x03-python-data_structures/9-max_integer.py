#!/usr/bin/python3
def max_integer(my_list=[]):
    big_int = int(my_list[0]) if len(my_list) > 0 else None
    for val in my_list:
        if int(val) >= big_int:
            big_int = int(val)
    return big_int