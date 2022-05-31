#!/usr/bin/python3
"""Class BaseGeometry"""


class BaseGeometry():
    """A class Father of the geometrics figures"""
    def area(self):
        """Public instance method that raises an Exception
        the message area() is not implemented"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Public method that validate a value"""
        if type(value) != int:
            raise TypeError(f'{name} must be an integer')
        if value <= 0:
            raise ValueError(f'{name} must be greater then 0')
