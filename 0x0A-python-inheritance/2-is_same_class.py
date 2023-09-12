#!/usr/bin/python3
"""
This function return true if the object is exactly
the instance of the class

Author: @SOULEYTECH
Date: 11/09/2023
"""


def is_same_class(obj, a_class):
    """
    This function return true if is exactly the same class
    otherwise false

    args:
    :param obj(class): the first arguments
    :param a_class(class): The second class
    :return: True or False
    """
    return isinstance(obj, a_class) & issubclass(obj.__class__, a_class)
