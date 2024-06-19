#!/usr/bin/python3
# 0-rectangle.py
"""Define a class Rectangle"""


class Rectangle:
    """ Represent a  Rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Initialize a new rectangle

        Args:
            width(int): The width of the rectangle
            height(int): The height of the rectangle

        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def __str__(self):
        """Return a string representation of the
           rectangle with the character #

        """
        result = ""
        if self.__height == 0 or self.__width == 0:
            return result

        for _ in range(self.__height):
            result += str(self.print_symbol) * self.__width + "\n"
        return result[:-1]

    def __repr__(self):
        """Return a string representation of the rectangle for eval()"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Print a message when an instance is deleted"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle based on the area

        Args:
            rect_1(int): the area of rectangle_1
            rect_2(int): the area of rectangle_2

        Raise:
            TypeError: if rect_1 or rect_2 not instance of Rectangle

        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        area_1 = rect_1.width * rect_1.height
        area_2 = rect_2.width * rect_2.height
        return rect_1 if area_1 >= area_2 else rect_2
