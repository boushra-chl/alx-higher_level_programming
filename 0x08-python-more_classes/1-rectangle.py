#!/usr/bin/python3
"""module that defines a rectangle"""


class Rectangle:
    """class that defines a real rectangle"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
    def width(self):
        return self.__width
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be >= 0")
        self.__width = value
    def height(self):
        return self.__height
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be >= 0")
        self.__height = value
