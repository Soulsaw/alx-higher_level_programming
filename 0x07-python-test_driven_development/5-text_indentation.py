#!/usr/bin/python3
"""
This function add to integer
Author: @SOULEYTECH
Date: 05/09/2023
"""


def text_indentation(text):
    """
    This function print the text
    Args:
        :param text(str): The text to displays
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    new_line = False
    for c in text:
        if new_line:
            if c == " ":
                continue
            new_line = False
        if c in ".?:":
            print('{}'.format(c+"\n"))
            new_line = True
        else:
            print("{}".format(c), end='')
