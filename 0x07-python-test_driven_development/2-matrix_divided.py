#!/usr/bin/python3
"""
This function divise all elements of the mstrix
Author: @SOULEYTECH
Date: 06/09/3023
"""


def matrix_divided(matrix, div):
    """This function divise the elements of integer
    :param matrix(list) : is the nested
    :param div(int): The dividant"""
    ma_list = []
    for row in matrix:
        for item in row:
            if type(item) not in [int, float]:
                raise TypeError("matrix must \
                    be a matrix (list of lists) of integers/floats")
        ma_list.append(len(row))
    if len(ma_list) > 0:
        for i in ma_list:
            if i != ma_list[0]:
                raise TypeError("Each row of the \
                    matrix must have the same size")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []
    for row in matrix:
        new_row = []
        for item in row:
            new_row.append(round(item / div, 2))
        new_matrix.append(new_row)
    return new_matrix


if __name__ == "__main__":
    import doctest
    doctest.testfile('tests/2-matrix_divided.txt')
