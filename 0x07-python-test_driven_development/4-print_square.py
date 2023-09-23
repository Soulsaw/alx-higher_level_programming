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
    if type(size) in [int, float]:
        if type(size) is float and size < 0:
            raise TypeError("size must be an integer")
        else:
            if size >= 0:
                for i in range(int(size)):
                    for j in range(int(size)):
                        print("{}".format("#"), end='')
                    print()
            else:
                raise ValueError("size must be >= 0")
    else:
        raise TypeError("size must be an integer")


if __name__ == "__main__":
    import doctest
    doctest.testfile("./tests/4-print_square.txt")
