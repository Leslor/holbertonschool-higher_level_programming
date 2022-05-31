#!/usr/bin/python3
"""Function that adds a new attributo to an object if it's possible"""


def add_attribute(object, name, value):
    """function that returns True if the object is
    exactly an instance of the specified class ;
    otherwise False
    """

    if setattr(object, name, value) is not None:
        raise TypeError("can't add new attribute")
