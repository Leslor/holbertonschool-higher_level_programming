#!/usr/bin/python3


def fizzbuzz():
    print("1 ", end="")
    for a in range(2, 101):
        if a % 3  == 0 and a % 5 == 0:
            print("FizzBuzz ", end="")
        elif a % 3 == 0:
            print("Fizz ", end="")
        elif a % 5 == 0:
            print("Buzz ", end="")
        else:
            print(f"{a} ", end="")
