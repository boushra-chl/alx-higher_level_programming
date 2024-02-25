#!/usr/bin/python3
"""module that creates a class"""


class Base:
    """class Base"""
    __nb_objects = 0
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects = Base.__nb_objects + 1
            self.id = Base.__nb_objects
