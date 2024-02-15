#!/usr/bin/python3
"""

a module that contains one function to divied matrix by a number

"""
def matrix_divided(matrix, div):
    """Return a matrix divided by an integer or float

    Args:
        matrix: (list of lists) of integers or floats
        div: integer or float

    Returns:
        divided matrix
    
    Raises:
        TypeError: if matrix or div are not of integers or floats
        TypeError: if rows have not the same size
        ZeroDivisionError: if div is 0
    """
    divided_matrix = []
    len_first_row = len(matrix[0])
    if div == 0:
        raise ZeroDivisionError("division by 0")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    for row in matrix:
        if len(row) != len_first_row:
            raise TypeError("Each row of the matrix must have the same size")
        for x in row:
            if not isinstance(x, int) and not isinstance(x, float):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            else:
                x = x / div
                x_rounded = round(x, 2)
                divided_matrix.append(x_rounded)
    return divided_matrix

