#!/usr/bin/python3
# 5-base_geometry.py
"""Define an empty class"""


class BaseGeometry():
    """ Represent base class"""
    pass

    def area(self):
        """Define public instance method

        Raise:
            Exception: with the message
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """ Public instance method  that validates value

        Args:
            name(string): some string
            vlaue(int): value to check

        Raise:
            TypeError: if value is not an integer
            ValueError: if value is less or equal to 0
        """
        if not isinstance(value, int):
            raise TypeError('{} must be an integer'.format(name))

        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
