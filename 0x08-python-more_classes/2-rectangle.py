#!/usr/bin/python3
"""Class Rectangle"""


class Rectangle():
    """A class Square with its constructor method"""
    def __init__(self, width=0, height=(0, 0)):
        """
        Args:
            width: width of Rectangle. Private instance attribute.
            height: height of Rectangle. Private instance attribute.
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """Getter Method"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter Method
            Args:
                value: width of Rectangle
        """
        if isinstance(value, int):
            if value < 0:
                raise ValueError('width must be >= 0')
            self.__width = value
        else:
            raise TypeError('width must be an integer')

    @property
    def height(self):
        """Getter Method"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter Method
            Args:
                value: height of Rectangle
        """
        if isinstance(value, int):
            if value < 0:
                raise ValueError('height must be >= 0')
            self.__height = value
        else:
            raise TypeError('height must be an integer')

    def area(self):
        """Returns the current square area"""
        area_r = self.__width * self.__height
        return area_r

    def perimeter(self):
        """Returns the current rectangle perimeter"""
        perimeter_r = self.__width * 2 + self.__height * 2
        return perimeter_r
