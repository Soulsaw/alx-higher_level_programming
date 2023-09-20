#!/usr/bin/python3
import json
"""
This function Create an object from a "JSON file"

Author: @SOULEYTECH
Date: 20/09/2023

"""


def load_from_json_file(filename):
    """
    This function create an object from de "json file"

    Args:
    :param filename(str): The is the name of file
    :return: Nothing
    """
    with open(filename, mode='r', encoding='utf-8') as f:
        return (json.loads(json.dumps(json.load(f))))
