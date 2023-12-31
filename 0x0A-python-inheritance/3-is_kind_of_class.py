#!/usr/bin/python3
"""
This function return true if the object is an
instance of, or if the object is an instance of a class that inherited from

Author: @SOULEYTECH
Date: 11/09/2023
"""


def is_kind_of_class(obj, a_class):
    """
    if the object is an instance of, or if
    the object is an instance of a class that inherited from

    args:
    :param obj(class): the first arguments
    :param a_class(class): The second class
    :return: True or False
    """
    return isinstance(obj, a_class)
