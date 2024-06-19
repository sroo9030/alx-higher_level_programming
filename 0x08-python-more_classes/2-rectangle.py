#!/usr/bin/python3
# 0-rectangle.py
"""Define a class Rectangle"""


class Rectangle:
    """ Represent a  Rectangle"""

    def __init__(self, width=0, height=0):
        """ Initialize a new rectangle

        Args:
            width(int): The width of the rectangle
            height(int): The height of the rectangle

        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ To retrieve the width of the rectangle"""
        return self.__width

    @property
    def height(self):
        """ To retrieve the height of the rectangle"""
        return self.__height

    @width.setter
    def width(self, value):
        """ To set the width of the rectangle

        Args:
            value(int): the value of the width

        Raise:
            TypeError: if the value not an integer
            ValueError: if the value not >= 0

        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """ To set the height of rectangle

        Args:
            value(int): the value of the height

        Raise:
            TypeError: if the value not an integer
            ValueError: if the value not >= 0

        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Return the area of the Rectangle"""
        return (self.__height * self.__width)

    def perimeter(self):
        """ Return the perimeter of the Rectangle"""
        if self.__height == 0 or self.__width == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))
