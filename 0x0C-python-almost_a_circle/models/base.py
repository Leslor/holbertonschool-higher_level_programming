#!/usr/bin/python3
"""Class Base"""
import json


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
