#!/usr/bin/python3
"""module that defines a rectangle"""


class Rectangle:
    """class that defines a real rectangle"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
    def width(self):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be >= 0")
        return self.width
    def height(self):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be >= 0")
        return self.height
