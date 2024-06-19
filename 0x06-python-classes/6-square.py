#!/usr/bin/python3
# 0-square.py
"""Define a class Square """


class Square():
    """Represent a Square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square

        Args:
            size(int): The size of the square
            position(int): Tuple of 2 positive integers

        Raises:
            TypeError: if the size not an integer,
                or position not a tuple of 2 positive integers
            ValueError: if the size not >= 0

        """
        self.__size = size
        self.__position = position

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        if not isinstance(position, tuple) or len(position) != 2 or \
           not all(isinstance(coord, int) and
           coord >= 0 for coord in position):
            raise TypeError("position must be a tuple of 2 positive integers")

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

    @property
    def position(self):
        """To retrieve the position

        """
        return self.__position

    @size.setter
    def size(self, value):
        """To set the size

        Args:
            value(int): The value of the size

        Raises:
            TypeError: if the value not an integer
            ValueError: if the value not >= 0

        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        elif value < 0:
            raise ValueError("size must be >= 0")

        else:
            self.__size = value

    @position.setter
    def position(self, value):
        """To set the position

        Args:
            value(int): 2 positive integers

        Raise:
            TypeError: if the value is not a tuple of 2 positive integers

        """
        if not isinstance(value, tuple) or len(value) != 2 or \
           not all(isinstance(coord, int) and coord >= 0 for coord in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def my_print(self):
        """Print he square with the character #

        """
        if self.__size == 0:
            print()
            return

        for _ in range(self.__position[1]):
            print()

        for _ in range(self.__size):
            for _ in range(self.__position[0]):
                print(" ", end="")

            for _ in range(self.__size):
                print("#", end="")
            print()
