#!/usr/bin/python3
"""

This module has one function the adds two integers

"""
def add_integer(a, b=98):
    """Return the sum of two integers or floats as integers

    Args:
        a: first integer
        b: second integer

    Returns:
        Sum of a and b

    Raises:
        TypeError: if a or b are not integers or floats
    """
    som = 0
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    som = int(a) + int(b)
    return som
