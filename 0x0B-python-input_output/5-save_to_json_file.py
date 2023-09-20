#!/usr/bin/python3
"""
This function write a object to a text file

Author: @SOULEYTECH
Date: 20/09/2023

"""
import json


def save_to_json_file(my_obj, filename):
    """
    This function write an object to the text file

    Args:
    :param my_obj(str): The is the string
    :param filename(str): Is the name of the file
    :return: The a text file
    """
    with open(filename, mode='w', encoding='utf-8') as f:
        json.dump(my_obj, f)
