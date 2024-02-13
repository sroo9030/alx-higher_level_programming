#!/usr/bin/python3
# 4-inherits_from.py
"""Define class-checking function"""


def inherits_from(obj, a_class):
    """Check if the object is exactly an instance of the
       (directly or indirectly) specified class

    Args:
        obj(anytype): the object to check
        a_class(antype): the class to check an obj with

    Return:
        True if the object is exactly an instance of the
        (directly or indirectly) specified class, otherwise False

    """
    return isinstance(obj, a_class) and type(obj) is not a_class
