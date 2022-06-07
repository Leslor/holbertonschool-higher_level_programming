#!/usr/bin/python3
"""Class Rectagle"""
from models.base import Base


class Rectangle(Base):
    """
    Class Rectangle that inherits from Base
    Args:
        width: ...
        height: ..
        x: ...
        y: ...
        id : ..
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor of the Rectangle Class"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
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

        symbol = "#"
        if self.__width == 0 or self.__height == 0:
            print()
        else:
            rectangle = ' ' * self.__x + str(symbol) * (self.__width)
            if self.__y > 0:
                print('\n' * (self.__y - 1))
            rectg_format = [rectangle for i in range(self.__height)]
            print('\n'.join(rectg_format))

    def __str__(self):
        """Private Method that  prints the Rectangle with the character # """
        return f'[Rectangle] ({self.id}) {self.__x}/{self.__y} -' \
               f' {self.__width}/{self.__height}'

    def update(self, *args, **kwargs):
        """Private Method that  prints the Rectangle with the character # """
        if len(args) > 0:
            atr_va = [self.id, self.width, self.height, self.x, self.y]
            i = 0
            while i < len(atr_va) and i < len(args):
                atr_va[i] = args[i]
                i += 1
            self.__init__(atr_va[1], atr_va[2], atr_va[3], atr_va[4],
                          atr_va[0])
        elif len(kwargs) > 0:
            atr_value = {'id': self.id, 'width': self.width,
                         'height': self.height, 'x': self.x, 'y': self.y}
            for key_atr in atr_value.keys():
                for key, value in kwargs.items():
                    if key_atr == key:
                        atr_value[key_atr] = value
            self.__init__(atr_value.get('width'), atr_value.get('height'),
                          atr_value.get('x'), atr_value.get('y'),
                          atr_value.get('id'))
        else:
            return

    def to_dictionary(self):
        """Private Method that  prints the Rectangle with the character # """
        key_order = ('y', 'x', 'id', 'width', 'height')
        return {key_order[i]: getattr(self, key_order[i])
                for i in range(len(key_order))}
