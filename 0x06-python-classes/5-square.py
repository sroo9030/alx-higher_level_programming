#!/usr/bin/python3
# 0-square.py
"""Define a class Square """


class Square():
    """Represent a Square"""

    def __init__(self, size=0):
        """Initialize a new Square

        Args:
            size(int): The size of the square

        Raises:
            TypeError: size must be an integer
            ValueError: size must be >= 0

        """
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Calculate current square area

        Return:
            the current square area

        """
        return self.__size**2

    @property
    def size(self):
        """To retrieve the size

        """
        return self.__size

    @size.setter
    def size(self, value):
        """To set the size

        Args:
            value(int): The value of the size

        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        elif value < 0:
            raise ValueError("size must be >= 0")

        else:
            self.__size = value

    def my_print(self):
        """Print he square with the character #

        """
        if self.__size == 0:
            print()
            return

        for _ in range(0, self.__size):
            for _ in range(0, self.__size):
                print("#", end="")
            print()
