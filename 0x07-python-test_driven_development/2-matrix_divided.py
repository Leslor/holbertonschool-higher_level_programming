#!/usr/bin/python3
"""Function that divides all elements of a matrix."""


def matrix_divided(matrix, div):
    """Returns a new matrix
    Raises:
        TypeError: if one of the arguments are not int or float
        TypeError: if Each row of the matrix must have the same size
        TypeError: if div is not a number (integer or float)
        ZeroDivisionError: if div is equal to 0
    """
    if not isinstance(div, (int, float)):
        raise TypeError('div must be an number')

    if div == 0:
        raise ZeroDivisionError('division by zero')

    size = len(matrix[0])
    for i in matrix:
        if size != len(i):
            raise TypeError('Each row of the matrix must have the same size')
        for j in i:
            if not isinstance(j, (int, float)) or not isinstance(i, list):
                raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
    n_m = list(map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix))
    return n_m
