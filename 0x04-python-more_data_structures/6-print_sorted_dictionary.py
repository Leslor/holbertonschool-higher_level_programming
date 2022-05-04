#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    """ function that replaces or adds key/value in a dictionary"""
    for i in sorted(a_dictionary):
        print("{}: {}".format(i, a_dictionary.get(i)))
