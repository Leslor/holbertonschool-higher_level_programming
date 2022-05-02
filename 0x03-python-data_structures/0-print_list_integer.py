#!/usr/bin/python3


def print_list_integer(my_list=[]):
    """Function that prints all integers of a list """
    if len(my_list) > 0:
        print(*my_list, sep='\n')
