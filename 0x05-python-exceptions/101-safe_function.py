#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    """function that executes a function safely."""
    try:
        return fct(args[0], args[1])
    except BaseException as x:
        print(f"Exception: {x}", file=sys.stderr)
        return None
