#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    """Function that print a matrix of integers"""
    if matrix:
        for i in matrix:
            size, length = 1, len(i)
            for j in i:
                if size == length:
                    print("{:d}".format(j), end="")
                else:
                    print("{:d}".format(j), end=" ")
                size += 1
            print()
