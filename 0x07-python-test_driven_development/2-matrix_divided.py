#!/usr/bin/python3
# 2-matrix_divided.py
"""
Define a function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix.

    Args:
        matrix (list): A list of lists of integers or floats.
        div (int or float): The number by which to divide each element

    Raises:
        TypeError: If the matrix is not a list of lists of integers or floats,
                   if any row of the matrix is not the same size,
                   if any element of the matrix is not an int or float,
                   or if div is not a number.
        ZeroDivisionError: If div is 0.

    Returns:
        list of lists: A new matrix with elements divided by div
        and rounded to 2 decimal places.
    """
    if not isinstance(matrix, list) or not all(
        isinstance(row, list) for row in matrix
    ):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    if not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(num / div, 2) for num in row] for row in matrix]
