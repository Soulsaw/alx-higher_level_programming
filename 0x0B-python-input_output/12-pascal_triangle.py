#!/usr/bin/python3
"""
This function return the triangle of pascal

Author: @SOULEYTECH
Date: 14/09/2023

"""


def pascal_triangle(n):
    """
    This function permit to return the triangle of pascal
    for the n row
    Args:
    :param n(int): The number of row of the triangle
    :return: triangle of pascal
    """
    if n <= 0:
        return []
    pascal = []
    for i in range(0, n, 1):
        row = []
        for j in range(0, i + 1, 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                row_ext = len(pascal)
                row.append(pascal[row_ext - 1][j] + pascal[row_ext - 1][j - 1])
        pascal.append(row)
    return pascal
