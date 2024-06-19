#!/usr/bin/python3
# 4-print_square.py
"""Define a function that prints a square"""


def print_square(size):
    """ a function that prints a square with the character #

    Args:
       size(int): the size length of the square

    Raise:
        TypeError: if the size is not an integer
        ValueError: if size is less than 0
        TypeError: if size is a float and less than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for i in range(0, size):
        for j in range(0, size):
            if j != (size - 1):
                print("#", end="")
            else:
                print("#")
