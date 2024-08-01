#!/usr/bin/python3
# 3-say_my_name.py
"""Define a function that prints Name"""


def say_my_name(first_name, last_name=""):
    """ a function that prints My name

    Args:
        first_name(string): the first name
        last_name()string: the last name

    Raise:
        TypeError: if the first or last name is not string

    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name).strip())
