#!/usr/bin/python3
"""
This function permit to read in the file

Author: @SOULEYTECH
Date: 14/09/2023

"""


def write_file(filename="", text=""):
    """
    This function permit to read in the file

    Args:
    :param filename(str): The is the name of file
    :return: Nothing
    """
    with open(filename, mode='w', encoding='utf-8') as read_f:
        nb_read = read_f.write(text)
        read_f.close()
    return nb_read
