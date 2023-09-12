#!/usr/bin/python3
"""
TThis class inherit from list

Author: @SOULEYTECH
Date: 11/09/2023
"""


class MyList(list):
    """
    THis class inherit from list

    args:

    """

    def __init__(self):
        """
        This is the __init__method

        Args:
        return nothing
        """
        self.list = list()

    def print_sorted(self):
        """
        This function print the elements of the list in the sortest
        format

        args:
        return: Print the different elements
        """
        newlist = [x for x in self]
        sort_list = sorted(newlist)
        list_len = len(sort_list)
        print("{}".format("["), end='')
        for i in range(list_len):
            print("{:d}{}".format(
                sort_list[i], ", " if i < list_len - 1 else ''), end='')
        print("]")

if __name__ == "__main__":
    import doctest
    doctest.testfile("./tests/1-my_list.txt")
