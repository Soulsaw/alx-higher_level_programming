#!/usr/bin/python3
"""
This class define a rectangle

Author: @SOULEYTECH
Date: 04/09/2023
"""


class Rectangle:
    """
    This class define the empty rectangle class

    Args:
        Nothing
    """
    def __init__(self, width=0, height=0):
        """
        This is the __init__ method

        Args:
            :param width (int): This is the width of the rectangle
            :param height (int): This is the height of the rectangle
            :return : Nothing
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        This methode permit to retrieve the value of the width

        Args:
            :return : The value of the width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        This method permit to set the value of thw width

        Args:
            :param value (int): This is the value to set
            :return : Nothing
        """
        if type(value) is int:
            if value >= 0:
                self.__width = value
            else:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """
        This methode permit to retrieve the value of the height

        Args:
            :return : The value of the height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        This method permit to set the value of thw height

        Args:
            :param value (int): This is the value to set
            :return : Nothing
        """
        if type(value) is int:
            if value >= 0:
                self.__height = value
            else:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")

    def area(self):
        """
        This methode return the rectangle area

        Args:
            :return : The rectangle area
        """
        return self.width * self.height

    def perimeter(self):
        """
        This method return the perimeter of the rectangle

        Args:
            :return : The perimeter of the rectangle
        """
        return (self.width + self.height) * 2
