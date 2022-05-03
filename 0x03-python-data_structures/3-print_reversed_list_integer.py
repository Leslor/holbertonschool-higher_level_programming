#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    """Function that prints all integers
       a list, in reverse order"""
    my_list = my_list[::-1]
    for i in my_list:
        print(i)
