#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """
    matrix: Is a matrix

    """
    for lin in matrix:
        ln = len(lin)
        for i in range(ln):
            print("{:d}{}".format(lin[i], ' ' if i < ln - 1 else ''), end='')
        print()
