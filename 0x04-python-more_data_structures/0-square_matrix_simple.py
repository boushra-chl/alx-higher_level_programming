#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    sqrt_matrix = []
    for row in matrix:
        sqrt_row = [x**2 for x in row]
        sqrt_matrix.append(sqrt_row)
    return sqrt_matrix
