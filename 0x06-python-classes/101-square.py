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
        position (tuple) : It's the position of tuple
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        This is the documentation of the __init__ method

        Args:
            size (int) : This is the size of the square
            Position (tuple) : This is the positionof the element
        """
        self.size = size
        self.position = position

    def __str__(self):
        """
        This function print the square of the # is size is more than 0

        """
        squares = ""
        if self.size == 0:
            return "\n"
        else:
            for g in range(self.position[1]):
                squares += "\n"
            for i in range(self.size):
                for k in range(self.position[0]):
                    squares += " "
                for j in range(self.size):
                    squares += "#"
                squares += "\n"
            return squares

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

    @property
    def position(self):
        """
        This method permit to get the value of the tuple position
        :return: The position of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        This method set the value of the position
        :param value: This is the value to set on the position
        :return: Nothing
        """
        if type(value) is tuple and len(value) == 2 and \
                value[0] >= 0 and value[1] >= 0:
            self.__position = value
        else:
            raise TypeError("position must be a \
tuple of 2 positive integers")

    def area(self):
        """
        This is the function that return the area of the square

        Return: The area of the square
        """
        return self.size ** 2

    def my_print(self):
        """
        This function print the square of the # is size is more than 0

        """
        if self.size == 0:
            print()
        else:
            for i in range(self.size):
                for k in range(self.position[0]):
                    print("{}".format(" "), end='')
                for j in range(self.size):
                    print("{}".format("#"), end='')
                print()
