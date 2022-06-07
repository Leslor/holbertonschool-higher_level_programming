#!/usr/bin/python3
"""Class Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    class Square that inherits from Rectangle
    Args:
        size: ...
        x: ...
        y: ...
        id: ...
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter Method"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter Method
        Args:
            value: size of Square
        """
        self.width = value
        self.height = value

    def __str__(self):
        """__str__ method"""
        return f'[Square] ({self.id}) {self.x}/{self.y} - {self.width}'

    def update(self, *args, **kwargs):
        """update method"""
        if len(args) > 0:
            atr_va = [self.id, self.size, self.x, self.y]
            i = 0
            while i < len(atr_va) and i < len(args):
                atr_va[i] = args[i]
                i += 1
            self.__init__(atr_va[1], atr_va[2], atr_va[3], atr_va[0])
        elif len(kwargs) > 0:
            atr_value = {'id': self.id, 'size': self.width,
                         'x': self.x, 'y': self.y}
            for key_atr in atr_value.keys():
                for key, value in kwargs.items():
                    if key_atr == key:
                        atr_value[key_atr] = value
            self.__init__(atr_value.get('size'), atr_value.get('x'),
                          atr_value.get('y'), atr_value.get('id'))
        else:
            return

    def to_dictionary(self):
        """to_dictionary method"""
        key_order = ('id', 'x', 'size', 'y')
        return {key_order[i]: getattr(self, key_order[i])
                for i in range(len(key_order))}
