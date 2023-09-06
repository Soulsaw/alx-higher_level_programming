#!/usr/bin/python3
"""
This function say hello
Author: @SOULEYTECH
Date: 05/09/2023
"""


def say_my_name(first_name, last_name=""):
    """This function permit to say hello
        :param first_name(str) : The first_name
        :param last_name(str) : The last_name"""
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    elif type(last_name) is not str:
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))


if __name__ == "__main__":
    import doctest
    doctest.testfile("./tests/3-say_my_name.txt")
