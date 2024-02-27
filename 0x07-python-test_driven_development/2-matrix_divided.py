#!/usr/bin/python3
# 2-matrix_divided.py
"""Define a function that divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix

    Args:
        matrix(list): a list of lists of integers or floats
        dev(int of float): a number

    Raise:
        TypeError: If the matrix is not a list of lists or
                   if the divisor is not an int or float.
        ZeroDivisionError: If the divisor is 0.
        TypeError: If any element of the matrix is not an int or float.
        TypeError: If any row of the matrix is not of the same size.

    Return:
        list of lists: A new matrix with elements divided by
        the divisor and rounded to 2 decimal places.
    """
    if type(div) not in (int, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists)\
                         of integers/floats")

    if any(len(row) != len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError("matrix must be a matrix (list of lists)\
                         of integers/floats")

    result = []
    for row in matrix:
        new_row = []
        for num in row:
            new_row.append(round(num / div, 2))
        result.append(new_row)

    return result
