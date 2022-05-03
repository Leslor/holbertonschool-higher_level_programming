#!/usr/bin/python3


def max_integer(my_list=[]):
    """Function that finds the biggest integer of a list"""
    if len(my_list) <= 0:
        return None
    max_value = my_list[0]
    for i in my_list:
        max_value = i if i > max_value else max_value
    return (max_value)
