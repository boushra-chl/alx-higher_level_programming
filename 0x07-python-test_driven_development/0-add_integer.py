#!/usr/bin/python3
def add_integer(a, b=98):
    som = 0
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    som = int(a) + int(b)
    return som
if __name__ == "__main__":
    import doctest
    doctest.testmod()
