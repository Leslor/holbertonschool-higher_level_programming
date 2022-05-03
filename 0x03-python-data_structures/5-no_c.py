#!/usr/bin/python3


def no_c(my_string):
    """Function that remove all character
       c and C from a string"""
    my_string = [i for i in my_string]
    for i in range(len(my_string) - 1):
        if my_string[i] == 'c' or my_string[i] == 'C':
            my_string[i] = ''
    return(''.join(my_string))
