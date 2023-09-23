#!/usr/bin/python3
"""
This is the Rectangle clas inherit from the BaseGeometry class

Author: @SOULEYTECH
Date: 23/09/2023
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    This is an empty class BaseGeometry

    args:
    return nothing
    """
    def __init__(self, width, height):
        """This is the __init__ method
        It's permit to create a constructor of the class
        Args:
            :param width(int): The width of the rectangle
            :param height(int): The height of the rectangle
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """This function return the area of the rectangle

        Args:
            :return: The area of the rectangle
        """
        return (self.__width * self.__height)

    def __str__(self):
        """
        This function return the string representation of the class
        """
        return "[{}] {}/{}".format(self.__class__.__name__,
                                   self.__width, self.__height)
