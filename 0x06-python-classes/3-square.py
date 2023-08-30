#!/usr/bin/python3
"""
This class define a Square

Author: @SOULEYTECH
Date: 30/08/2023

"""


class Square:
    """
    This class define a square with the attribute size

    Attributes:
        size (int) : This is the size of the square
    """
    def __init__(self, size=0):
        """
        This is the documentation of the __init__ method

        Args:
            size (int) : This is the size of the square
        """
        if type(size) is int:
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
    
    def area(self):
        """
        This is the function that return the area of the square

        Return: The area of the square
        """
        return self.__size ** 2
