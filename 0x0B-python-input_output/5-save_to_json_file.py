#!/usr/bin/python3
"""Function that appends a string at the end of a text
    file (UTF8) and returns the number of characters added"""
import json


def save_to_json_file(my_obj, filename):
    """Returns the number of characters added """

    with open(filename, 'w', encoding="utf-8") as f:
        content = f.write(json.dumps(my_obj))
    return content
