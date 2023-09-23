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
        self.validator(height, "height")
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
        self.validator(width, "width")
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
        if type(x) is int:
            if x >= 0:
                self.__x = x
            else:
                raise ValueError("x must be >= 0")
        else:
            raise TypeError("x must be an integer")

    @property
    def y(self):
        """This function retrieve the value of the y attribute
        """
        return self.__y

    @y.setter
    def y(self, y):
        """This function permit to set the value of the y attribute
        """
        if type(y) is int:
            if y >= 0:
                self.__y = y
            else:
                raise ValueError("y must be >= 0")
        else:
            raise TypeError("y must be an integer")

    def validator(self, value, name=""):
        """This function permit to valida an attributes
        """
        if type(value) is int and isinstance(value, int):
            if value < 0:
                raise ValueError("{} must be > 0".format(name))
        else:
            raise TypeError("{} must be an integer".format(name))

    def area(self):
        """This method return the area of the rectangle instance
        """
        return (self.width * self.height)

    def display(self):
        """This method permit to print in the stdout a rectangle of - #
        """
        for k in range(self.y):
            print()
        for i in range(self.height):
            for k in range(self.x):
                print(" ", end='')
            for j in range(self.width):
                print("{}".format("#"), end='')
            print()

    def __str__(self):
        """This is the __str__ method
        This method permit to describe string representation
        of the class instance
        """
        return "[{}] ({}) {}/{} - {}/{}" \
            .format(self.__class__.__name__, self.id,
                    self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """This method permit to update the constructor
        With the tuple of arguments

        Args:
            Is the tuple of arguments
            :param args(tuple): The first arguments
            :param kwargs(dictionary): The seconds arguments
        """
        self.id = args[0] if len(args) > 0 else kwargs.get("id") \
            if kwargs.get("id") is not None else self.id
        self.width = args[1] if len(args) > 1 else kwargs.get("width") \
            if kwargs.get("width") is not None else self.width
        self.height = args[2] if len(args) > 2 else kwargs.get("height") \
            if kwargs.get("height") is not None else self.height
        self.x = args[3] if len(args) > 3 else kwargs.get("x") \
            if kwargs.get("x") is not None else self.x
        self.y = args[4] if len(args) > 4 else kwargs.get("y") \
            if kwargs.get("y") is not None else self.y
