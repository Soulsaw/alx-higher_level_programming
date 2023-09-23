#!/usr/bin/python3
"""This class inherit from the Rectangle class

Author: @SOULEYTECH
Date: 22/09/2023
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """This class describe a square
    Args:
        :param Rectangle(): The parent class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """This is the init methods that permit to init the constructor

        Args:
            :param id (int)
            :param size (int)
            :param x (int)
            :param y (int)
            :return: Nothing
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        """
        return self.width

    @size.setter
    def size(self, size):
        """
        """
        self.width = size
        self.height = size

    def __str__(self):
        """This is the __str__ method
        This method permit to describe string representation
        of the class instance
        """
        return "[{}] ({}) {}/{} - {}" \
            .format(self.__class__.__name__, self.id,
                    self.x, self.y, self.width)

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
        self.size = args[1] if len(args) > 1 else kwargs.get("size") \
            if kwargs.get("size") is not None else self.size
        self.x = args[2] if len(args) > 2 else kwargs.get("x") \
            if kwargs.get("x") is not None else self.x
        self.y = args[3] if len(args) > 3 else kwargs.get("y") \
            if kwargs.get("y") is not None else self.y
