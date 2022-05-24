#!/usr/bin/python3
"""Class Rectangle"""


class Rectangle():
    """A class Square with its constructor method"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Args:
            width: width of Rectangle. Private instance attribute.
            height: height of Rectangle. Private instance attribute.
        """
        self.height = height
        self.width = width
        type(self).number_of_instances += 1

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
        if self__width == 0 or self.__height == 0:
            return 0
        perimeter_r = self.__width * 2 + self.__height * 2
        return perimeter_r

    def __print_rectangle(self):
        """Private Method that  prints the Rectangle with the character # """
        rectangle = ''
        if self.__width == 0 or self.__height == 0:
            return rectangle
        else:
            for i in range(self.__height):
                for j in range(self.__width):
                    rectangle += str(self.print_symbol)
                if i != self.__height - 1:
                    rectangle += '\n'
        return rectangle

    def __str__(self):
        return self.__print_rectangle()

    def __repr__(self):
        return f'Rectangle({self.__width}, {self.__height})'

    def __del__(self):
        type(self).number_of_instances -= 1
        print('Bye rectangle...')

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Method that returns the biggest rectangle based on the area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')

        area_1 = rect_1.area()
        area_2 = rect_2.area()

        if area_1 >= area_2:
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        return cls(size)
