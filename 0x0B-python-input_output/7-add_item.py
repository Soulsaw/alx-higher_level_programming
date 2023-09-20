#!/usr/bin/python3
"""
This scripts add all arguments to a file
Date:20/09/2023
"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
filename = "add_item.json"
open(filename, mode='w+')
for i in range(len(sys.argv) - 1):
    save_to_json_file(sys.argv[i], filename)
load_from_json_file(filename)
