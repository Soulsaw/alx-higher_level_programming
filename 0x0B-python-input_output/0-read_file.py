#!/usr/bin/python3
"""
This function permit to read in the file

Author: @SOULEYTECH
Date: 14/09/2023

"""


def read_file(filename=""):
    """
    This function permit to read in the file

    Args:
    :param filename(str): The is the name of file
    :return: Nothing
    """
    read_f = open(filename, 'r')
    for ligne in read_f:
        print(ligne, end='')
    read_f.close()
