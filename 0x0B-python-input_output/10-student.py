#!/usr/bin/python3
"""class Student that defines a student """


class Student():
    """Public instance attributes:
        Args:
            first_name
            last_name
            age
    """
    def __init__(self, first_name, last_name, age):
        """Constructor Method"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Public method def to_json(self): that
        retrieves a dictionary representation
        of a Student instance"""
        dict_format = {}
        if type(attrs) == list:
            for i in attrs:
                if type(i) != str:
                    return (self.__dict__)
            for i in attrs:
                if i in self.__dict__:
                    dict_format[i] = self.__dict__[i]
            return dict_format
        return (self.__dict__)
