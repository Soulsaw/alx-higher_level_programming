#!/usr/bin/python3
"""
This function Create an object from a "JSON file"

Author: @SOULEYTECH
Date: 20/09/2023

"""
import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
filename = "add_item.json"
my_list = []
with open(filename, mode='a', encoding='utf-8') as f:
    """this is the management of the file block
    """
    try:
        my_list = load_from_json_file(filename)
    except /:
        my_list = []
    finally:
        for idx in range(1, len(sys.argv)):
            my_list.append(sys.argv[idx])
    save_to_json_file(my_list, filename)
    f.close()
