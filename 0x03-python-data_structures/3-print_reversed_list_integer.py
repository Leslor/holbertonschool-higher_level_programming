#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    """Function that prints all integers
       a list, in reverse order"""
    if len(my_list) >= 0:
        print(*my_list[::-1], sep='\n')
