#!/usr/bin/python3
"""Class MyInt"""


class MyInt(int):

    def eq(self, other):
        """Method eq"""
        return super().ne(other)

    def ne(self, other):
        """Method eq"""
        return super().eq(other)
