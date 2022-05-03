#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    """Function that prints all integers
       a list, in reverse order"""
    my_list.reverse()
    print(*my_list, sep='\n')
