#!/usr/bin/python3
"""
This function add to integer
Author: @SOULEYTECH
Date: 05/09/2023
"""


def print_square(size):
    """This function print a square of "#"
        :param size(int) : The size of square
        :return : Nothing"""
    if type(size) is not int or (type(size) is float and size < 0):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    else:
        for i in range(size):
            for j in range(size):
                print("{}".format("#"), end='')
            print()


if __name__ == "__main__":
    import doctest
    doctest.testfile("./tests/4-print_square.txt")
