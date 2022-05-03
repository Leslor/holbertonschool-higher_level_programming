#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    """Function that finds all multiples of 2 in a list."""
    is_mult = [True if i % 2 == 0 else False for i in my_list]
    return (is_mult)
