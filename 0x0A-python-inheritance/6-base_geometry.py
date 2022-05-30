#!/usr/bin/python3
"""Class BaseGeometry"""


class BaseGeometry():
    """A class Father of the geometrics figures"""
    def __init__(self):
        pass

    def area(self):
        """Public instance method that raises an Exception
        the message area() is not implemented"""
        raise Exception('area() is not implemented')
