#!/usr/bin/python3
"""Class Square"""


class Square():
    """A class Square with its constructor method"""
    def __init__(self, size=0):
        """
        Args:
            size: size of Square. Private instance attribute.
        """
        if isinstance(size, int):
            if size < 0:
                raise ValueError('size must be >= 0')
            self.__size = size
        else:
            raise TypeError('size must be an integer')
