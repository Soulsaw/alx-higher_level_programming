#!/usr/bin/python3
"""
This function add to integer
Author: @SOULEYTECH
Date: 05/09/2023
"""


def add_integer(a, b=98):
    """This function permit to add to integer
        :param a(int) : The first integer
        :param b(int) : The second integer"""
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    elif type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)


if __name__ == "__main__":
    import doctest
    doctest.testfile("./tests/0-add_integer.txt")
