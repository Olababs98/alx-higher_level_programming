#!/usr/bin/python3
"""Defines a print square"""


def print_square(size):
    """prints a square of size using the character '#'"""

    # Check if size is an integer or a float
    if not isinstance(size, int):
        if isinstance(size, float) and size.is_integer():
            size = int(size)
        else:
            raise TypeError("size must be an integer")

    # Check if size is >= 0
    if size < 0:
        raise ValueError("size must be >= 0")

    # Print the square
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("")
