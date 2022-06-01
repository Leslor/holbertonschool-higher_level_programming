#!/usr/bin/python3
"""function that reads a text file (UTF8) and prints it to stdout:"""


def read_file(filename=""):
    """Returns an integer: the addition of a and b"""
    with open(filename, encoding="utf-8") as f:
        content = f.read()
    print(content, end="")
