#!/usr/bin/python3


if __name__ == "__main__":
    """program that prints the number of and the list of its arguments."""
    import sys
    args = len(sys.argv) - 1
    if args == 0:
        print(f"{args} arguments.")
    elif args == 1:
        print(f"{args} argument:")
    else:
        print(f"{args} arguments:")
    list_format = [print(f"{i}: {sys.argv[i]}") for i in range(1, args + 1)]
