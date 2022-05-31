#!/usr/bin/python3
"""Class BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class Rectangle that inherits from
    BaseGeometry (7-base_geometry.py)."""

    def __init__(self, width, height):
        """Building Method"""
        self.__width = self.integer_validator('width', width)
        self.__height = self.integer_validator('height', height)
