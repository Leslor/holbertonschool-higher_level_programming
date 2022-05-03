#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    """Function that prints all integers
       a list, in reverse order"""
    if len(my_list) == 0:
        return None
    my_list.reverse()
    for i in my_list:
        print(f"{i:d}")
