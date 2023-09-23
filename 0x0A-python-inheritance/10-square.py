#!/usr/bin/python3
"""
This is the Rectangle clas inherit from the Rectangle class

Author: @SOULEYTECH
Date: 23/09/2023
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    This is an empty class BaseGeometry

    args:
    return nothing
    """
    def __init__(self, size):
        """This is the __init__ method
        It's permit to create a constructor of the class
        Args:
            :param size(int): The side of the square
        """
        super().integer_validator("size", size)
        self.__width = size
        self.__height = size

    def area(self):
        """This function return the area of the rectangle

        Args:
            :return: The area of the rectangle
        """
        return (self.__width ** 2)
