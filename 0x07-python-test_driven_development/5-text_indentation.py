#!/usr/bin/python3
"""
This function add to integer
Author: @SOULEYTECH
Date: 05/09/2023
"""

def text_indentation(text):
    """
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    for c in text:
        print('{}'.format(c if c not in ".?:" else c+"\n\n"), end='')