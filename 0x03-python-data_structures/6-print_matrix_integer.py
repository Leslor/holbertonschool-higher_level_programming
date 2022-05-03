#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    """Function that print a matrix of integers"""
    if len(matrix) > 0:
        for i in matrix:
            for j in i:
                print("{:d}".format(j), end=" ")
            print("")
    else:
        print()
