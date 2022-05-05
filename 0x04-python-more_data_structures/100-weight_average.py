#!/usr/bin/python3


def weight_average(my_list=[]):
    """ function that returns the weighted average of
    all integers tuple (<score>, <weight>)"""
    if my_list:
        A = sum(list(map(lambda x: x[0] * x[1], my_list)))
        B = sum(list(map(lambda x: x[1], my_list)))
        return A / B
    return 0
