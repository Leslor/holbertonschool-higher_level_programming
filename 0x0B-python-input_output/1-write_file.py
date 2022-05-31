#!/usr/bin/python3
"""function that writes a text file (UTF8) and prints it to stdout:"""


def write_file(filename="", text=""):
    """Returns the number of characters written """

    with open(filename, 'w', encoding="utf-8") as f:
        content = f.write(text)

    return content
