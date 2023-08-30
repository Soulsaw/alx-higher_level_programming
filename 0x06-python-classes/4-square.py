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
        self.size = size

    @property
    def size(self):
        """
        This method permit to get the value of the size
        :return: The size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        This method set the value of the size
        :param value: This is the value to set on the size
        :return: Nothing
        """
        if type(value) is int:
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """
        This is the function that return the area of the square

        Return: The area of the square
        """
        return self.size ** 2
