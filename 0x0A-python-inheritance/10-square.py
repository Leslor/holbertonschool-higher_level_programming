#!/usr/bin/python3
"""Class Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A rectangle"""
    def __init__(self, size):
        self.integer_validator('size', size)
        super().__init__(size, size)
        self.__width = size
        self.__height = size
