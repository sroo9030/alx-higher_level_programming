#!/usr/bin/python3
# 2-matrix_divided.py
"""Define a function that divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix

    Args:
        matrix(list): a list of lists of integers or floats
        dev(int of float): a number

    Raise:
        TypeError: the list of lists of integers or floats or
                   the row of the matrix not the same size or
                   the div is not a number
        ZeroDivisionError: div equal 0

    Return:
        a new matrix
    """
    if type(div) not in (int, float):
        TypeError("div must be a number")

    if div == 0:
        ZeroDivisionError("division by zero")

    if not all(isinstance(row, list) for row in matrix):
        TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if any(len(row) != len(matrix[0]) for row in matrix):
        TypeError("Each row of the matrix must have the same size")

    if not all(isinstance(num, (int, float)) for row in matrix for num in row):
        TypeError("matrix must be a matrix (list of lists)\
                       of integers/floats")

    result = []
    for row in matrix:
        new_row = []
        for num in row:
            new_row.append(round(num / div, 2))
        result.append(new_row)

    return result
