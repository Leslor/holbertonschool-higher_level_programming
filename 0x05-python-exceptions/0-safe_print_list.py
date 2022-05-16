#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    """function that prints x elements of a list."""
    element = 0
    for element in range(x):
        try:
            print(f'{my_list[element]}', end="")
            element += 1
        except IndexError:
            break
    print("")
    return element
