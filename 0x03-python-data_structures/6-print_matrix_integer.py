#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    """Function that print a matrix of integers"""
    if len(matrix) > 0:
        for i in matrix:
            i = [str(j) for j in i]
            print(' '.join(i))
