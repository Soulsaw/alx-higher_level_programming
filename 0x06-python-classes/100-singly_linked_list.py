#!/usr/bin/python3
"""
This is the class that defines the node of the singly linked lists

Author: @SOULEYTECH
Date: 30/08/2023

"""


class Node:
    """
    This class Node that defines a node of a singly linked list by

    Author: @SOULEYTECH
    Date: 30/08/2023

    """
    def __init__(self, data, next_node=None):
        """
        This is the doc of the init method

        Args:
            :param data(int) : This is the data of each Node
            :param next_node() :
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        This methode permit to get a data
        :return: The data of the current data
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        This method permit to set the value of the data
        Args:
            :param value(int) : This is the new value of the node
        """
        if type(value) is int:
            self.__data = value
        else:
            raise ValueError("data must be an integer")

    @property
    def next_node(self):
        """
        This method permit to retrieve the next_node value
        return: The next node value
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, next_node=None):
        """
        This method permit to set the next node
        Args:
            :param next_node() :
        """
        if type(next_node) is None or type(Node):
            self.__next_node = next_node
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """

    """
    def __init__(self):
        self.__head = None

    def __str__(self):
        return self.printList()

    def sorted_insert(self, value):
        top = Node(value, None)
        if self.__head is None:
            self.__head = top
        else:
            tmp = self.__head
            while tmp.next_node:
                tmp = tmp.next_node
            tmp.next_node = top

    def printList(self):
        my_list = ""
        tmp = self.__head
        while tmp:
            print(tmp.data)
            my_list += str(tmp.data) + "\n"
            tmp = tmp.next_node
        return (my_list)
