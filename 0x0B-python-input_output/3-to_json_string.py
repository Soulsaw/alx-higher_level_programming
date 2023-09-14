#!/usr/bin/python3
import json
"""
This function permit to read in the file

Author: @SOULEYTECH
Date: 14/09/2023

"""


def to_json_string(my_obj):
    """
    This function permit to read in the file

    Args:
    :param filename(str): The is the name of file
    :return: Nothing
    """
   return json.JSONEncoder().encode(my_obj)
