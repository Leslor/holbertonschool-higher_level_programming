#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    """function that computes the square value of all integers of a matrix"""
    return [list(map(lambda x: x**2, i)) for i in matrix]
