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
    __nb_objects = 0

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