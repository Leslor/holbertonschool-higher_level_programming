#!/usr/bin/python3


def safe_print_division(a, b):
    """ function that divides 2 integers and prints the result."""
    try:
        divition = a / b
    except ArithmeticError:
        divition = None
    finally:
        print('Inside result: {}'.format(divition))
    return divition
