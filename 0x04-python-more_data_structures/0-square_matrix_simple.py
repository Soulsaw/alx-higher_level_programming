#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """
    matrix: Is a matrix 3x3
    """
    new_matrix = []
    for lign in matrix:
        new_lig = []
        for x in lign:
            new_lig.append(x**2)
        new_matrix.append(new_lig)
    return new_matrix
