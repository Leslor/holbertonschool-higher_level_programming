#!/usr/bin/python3


class MyInt(int):

        def eq(self, other):
            return super().ne(other)
        def ne(self, other):
            return super().eq(other)
