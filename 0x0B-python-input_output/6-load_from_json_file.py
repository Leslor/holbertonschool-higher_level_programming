#!/usr/bin/python3
"""function that creates an Object from a “JSON file"""
import json


def load_from_json_file(filename):
    """Returns the number of characters added """

    with open(filename) as f:
        content = json.load(f)
        return content
