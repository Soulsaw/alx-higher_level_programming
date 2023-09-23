#!/usr/bin/python3
"""
This is an empty class BaseGeometry

Author: @SOULEYTECH
Date: 11/09/2023
"""


class BaseGeometry:
    """
    This is an empty class BaseGeometry

    args:
    return nothing
    """
    pass

    def area(self):
        """This method permit to raise exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """This function permit to validate a value

        Args:
            :param name(str): Is the name of value
            :param value(int): Is the value to valide
        """
        if type(value) is int:
            if value <= 0:
                raise ValueError("{} must be greater than 0".format(name))
        else:
            raise TypeError("{} must be an integer".format(name))


if __name__ == "__main__":
    import doctest
    doctest.testfile("./tests/7-base_geometry.txt")
