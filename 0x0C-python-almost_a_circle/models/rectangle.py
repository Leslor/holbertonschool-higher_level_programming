#!/usr/bin/python3
"""Class Rectagle"""
from models.base import Base


class Rectangle(Base):
    """class Rectangle that inherits from Base
    """
    symbol = "#"

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width, self.height = width, height
        self.x, self.y = x, y
        super().__init__(id)

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
            if value <= 0:
                raise ValueError('width must be > 0')
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
            if value <= 0:
                raise ValueError('height must be > 0')
            self.__height = value
        else:
            raise TypeError('height must be an integer')

    @property
    def x(self):
        """Getter Method"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter Method
        Args:
            value: height of Rectangle
        """
        if isinstance(value, int):
            if value < 0:
                raise ValueError('x must be >= 0')
            self.__x = value
        else:
            raise TypeError('x must be an integer')

    @property
    def y(self):
        """Getter Method"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter Method
        Args:
            value: height of Rectangle
        """
        if isinstance(value, int):
            if value < 0:
                raise ValueError('y must be >= 0')
            self.__y = value
        else:
            raise TypeError('y must be an integer')

    def area(self):
        """Returns the current square area"""
        area_r = self.__height * self.__width
        return area_r

    def display(self):
        """Private Method that  prints the Rectangle with the character # """
        if self.__width == 0 or self.__height == 0:
            print()
        else:
            rectangle = ' ' * self.__x + str(self.symbol) * (self.__width)
            if self.__y > 0:
                print('\n' * (self.__y - 1))
            rectg_format = [rectangle for i in range(self.__height)]
            print('\n'.join(rectg_format))

    def __str__(self):
        return f'[Rectangle] ({self.id}) {self.__x}/{self.__y} -' \
                f' {self.__width}/{self.__height}'

    def update(self, *args):
        if len(args) == 0:
            return
        atr_value = [self.id, self.width, self.height, self.x, self.y]
        i, len_atr, len_arg = 0, len(atr_value), len(args)
        while i < len_atr and i < len_arg:
            atr_value[i] = args[i]
            i += 1
        self.__init__(atr_value[1], atr_value[2],
                      atr_value[3], atr_value[4], atr_value[0])
