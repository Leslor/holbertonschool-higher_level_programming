#!/usr/bin/python3
"""Function is_kind_of_class"""


def is_kind_of_class(obj, a_class):
    """function that returns True if the object is
    exactly an instance of the specified class;
    otherwise False
    """
    if isinstance(obj, a_class):
        return True
    return False
