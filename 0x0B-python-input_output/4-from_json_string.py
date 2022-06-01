#!/usr/bin/python3
""" function that returns an object
    (Python data structure) represented
    by a JSON string:"""
import json


def from_json_string(my_str):
    """Returns an object  represented by JSON"""
    return json.loads(my_str)