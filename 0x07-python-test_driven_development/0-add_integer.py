#!/usr/bin/python3
# 0-add_integer.py
"""Defines an integer addition function."""


def add_integer(a, b=98):
    """
    Adds two integers and returns the result.

    Args:
        a (int): The first integer to be added.
        b (int, optional): The second integer to be added. Defaults to 98.

    Returns:
        int: The sum of the two integers.

    Raises:
        TypeError: If either `a` or `b` is not an integer.
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
