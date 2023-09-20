#!/usr/bin/python3
"""
This function return the json representation of string

Author: @SOULEYTECH
Date: 20/09/2023

"""
import json


def from_json_string(my_str):
    """
    This function json representation of string

    Args:
    :param my_str(str): The is the string
    :return: The json representation of string
    """
    return json.loads(my_str)
