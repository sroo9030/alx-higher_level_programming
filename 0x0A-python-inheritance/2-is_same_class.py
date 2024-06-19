#!/usr/bin/python3
# 2-is_same_class.py
"""Define class-checking function"""


def is_same_class(obj, a_class):
    """Check if the object is exactly an instance of the specified class

    Args:
        obj(anytype): the object to check
        a_class(antype): the class to check an obj with

    Return:
        True if the object is exactly an instance of the specified class,
        otherwise False

    """
    return type(obj) is a_class
