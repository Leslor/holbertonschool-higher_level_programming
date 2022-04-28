#!/usr/bin/python3


if __name__ == "__main__":
    """program that prints the result the addition of all arguments."""
    import sys
    print(sum([int(i) for i in sys.argv[1:]]))
