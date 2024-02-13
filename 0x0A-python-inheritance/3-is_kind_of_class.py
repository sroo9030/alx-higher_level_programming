#!/usr/bin/python3
# 3-is_kind_of_class.py
"""Define class-checking function"""


def is_kind_of_class(obj, a_class):
    """Check if the object is exactly an instance of the specified class

    Args:
        obj(anytype): the object to check
        a_class(antype): the class to check an obj with

    Return:
        True if the object is exactly an instance of the specified class,
        or if the object is an instance of a class that inherited from,
        the specified class, otherwise False

    """
    return isinstance(obj, a_class)
