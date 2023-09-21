#!/usr/bin/python3
"""This class inherit from the Base class

Author: @SOULEYTECH
Date: 21/09/2023
"""
from models.base import Base


class Rectangle(Base):
    """This class describe a rectangle and inh
    Args:
        :param ():
    """
    __nb_objects = 0

    def __init__(self, width, height, x=0, y=0, id=None):
        """This is the init methods that permit to init the constructor

        Args:
            :param id (int)
            :param width (int)
            :param height (int)
            :param x (int)
            :param y (int)
            :return: Nothing
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def height(self):
        """This methode permit to retrieve the value of the height
        """
        return self.__height

    @height.setter
    def height(self, height):
        """This function permit to set the value of the height
        """
        self.__height = height

    @property
    def width(self):
        """This function permit to retrieve the value of the widht attribute
        """
        return self.__width

    @width.setter
    def width(self, width):
        """This function permit to set the value of the width attribut
        """
        self.__width = width

    @property
    def x(self):
        """This function retrieve the value of the x attribute
        """
        return self.__x

    @x.setter
    def x(self, x):
        """This function set the value of the x attribute
        """
        self.__x = x

    @property
    def y(self):
        """This function retrieve the value of the y attribute
        """
        return self.__y

    @y.setter
    def y(self, y):
        """This function permit to set the value of the y attribute
        """
        self.__y = y
