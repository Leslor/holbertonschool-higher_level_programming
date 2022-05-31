#!/usr/bin/python3
"""Function inherits_from"""


def inherits_from(obj, a_class):
    """function that returns True if the object is
    exactly an instance of the specified class ;
    otherwise False
    """
    if issubclass(type(obj), a_class) and not type(obj) == a_class:
        return True
    return False
