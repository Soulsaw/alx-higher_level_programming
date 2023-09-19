#!usr/bin/python3
"""This class is the base class in the folder

Author: @SOULEYTECH
Date: 18/09/2023
"""


class Base:
    """This class is the base classe in this folder
    Args:
        :param ():
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """This is the init methods that permit to init the constructor

        Args:
            :param id (int)
            :return: Nothing
        """
        if id is not None:
            self.id = id
        else:
            self.increment()
            self.id = self.__nb_objects

    @classmethod
    def increment(self):
        """This class method permit to change the instance value
        of the private attribut
        """
        self.__nb_objects += 1