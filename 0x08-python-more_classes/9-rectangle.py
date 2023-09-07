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
        number_of_instances is the public attribute
    """
    number_of_instances = 0
    print_symbol = "#"

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
        type(self).number_of_instances += 1

    def __str__(self):
        """
        This is the __str__ method
        This method print the rectangle of "#"
        """
        rectange = ""
        if self.width == 0 or self.height == 0:
            return rectange
        else:
            for i in range(self.height):
                for j in range(self.width):
                    rectange += Rectangle.print_symbol
                if i < self.height - 1:
                    rectange += "\n"
        return rectange

    def __repr__(self):
        """
        This method represent the rectangle from this style
        Rectangle(width, height)
        """
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """
        This is __del__ method
        This method is handle if an instance is del
        decrement the number of instance
        """
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

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
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return (self.width + self.height) * 2

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        This function return the biggest of two rectangle
        """
        if isinstance(rect_1, Rectangle):
            if isinstance(rect_2, Rectangle):
                if rect_1.area() == rect_2.area():
                    return rect_1
                elif rect_1.area() > rect_2.area():
                    return rect_1
                else:
                    return rect_2
            else:
                raise TypeError("rect_2 must be an instance of Rectangle")
        else:
            raise TypeError("rect_1 must be an instance of Rectangle")

    @classmethod
    def square(cls, size=0):
        """
        """
        cls.width = size
        cls.height = size
        return cls
