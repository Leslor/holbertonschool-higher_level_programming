#!/usr/bin/python3
"""Function that prints a square with the character #."""


def print_square(size):
    """Returns nothing just print in the Stdout"
    Raises:
        TypeError: if size argument is not a integer
        ValueError: if size is < 0
    """
    if isinstance(size, int):
        if size < 0:
            raise ValueError('size must be >= 0')
    else:
        raise TypeError('size must be an integer')

    if size == 0:
        print()
    else:
        for i in range(size):
            for j in range(size):
                print("#", end="")
            print()
