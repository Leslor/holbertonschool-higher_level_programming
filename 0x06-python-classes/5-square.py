#!/usr/bin/python3
"""Class Square"""


class Square():
    """A class Square with its constructor method"""
    def __init__(self, size=0):
        """
        Args:
            size: size of Square. Private instance attribute.
        """
        self.__size = size

    @property
    def size(self):
        """Getter Method"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter Method
            Args:
                value: size of Square
        """
        if isinstance(value, int):
            if value < 0:
                raise ValueError('size must be >= 0')
            self.__size = value
        else:
            raise TypeError('size must be an integer')

    def area(self):
        """Returns the current square area"""
        result = self.__size * self.__size
        return result

    def my_print(self):
        """Function that prints in stdout the square with the character # """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
