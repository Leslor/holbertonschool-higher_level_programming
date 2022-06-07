#!/usr/bin/python3
"""Class Base"""
import json
from os.path import exists
import turtle

class Base():
    """class Base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """to_json_string method"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save_to_file method"""
        filename = f'{cls.__name__}.json'
        with open(filename, 'w') as f:
            if list_objs is None:
                return f.write("[]")
            inst_atribt = [instan.to_dictionary() for instan in list_objs]
            return f.write(cls.to_json_string(inst_atribt))

    @staticmethod
    def from_json_string(json_string):
        """from_json_string method"""
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Class method that returns an instance with
        all attributes already set"""
        dummy = cls(**dictionary)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Class instance that returns a list of instances"""
        filename = f'{cls.__name__}.json'
        if exists(filename) is False:
            return []
        with open(filename, 'r') as f:
            new_dict = cls.from_json_string(f.read())
            new_inst = [cls.create(**inst) for inst in new_dict]
            return new_inst

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Drawing Board and turtle"""
        wn = turtle.Screen()
        wn.bgcolor("#343434")
        wn.title("Shapes")
        fig = turtle.Turtle()
        fig.shape('turtle')
        fig.pensize(4)

        """Moving the Turtle"""
        for rectangle in list_rectangles:
            fig.hideturtle()
            fig.color('#1BDED9')
            fig.up()
            fig.goto(rectangle.x, rectangle.y)
            fig.down()
            for r in range(2):
                fig.forward(rectangle.width)
                fig.left(90)
                fig.forward(rectangle.height)
                fig.left(90)

        for square in list_squares:
            fig.hideturtle()
            fig.color('#2D70FF')
            fig.up()
            fig.goto(square.x, square.y)
            fig.down()
            for s in range(4):
                fig.forward(square.size)
                fig.left(90)
