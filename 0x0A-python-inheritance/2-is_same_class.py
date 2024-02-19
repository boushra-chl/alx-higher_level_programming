#!/usr/bin/python3
"""module that returns True or false"""


def is_same_class(obj, a_class):
    """function that returns True or false"""
    if type(obj) == a_class:
        return True
    else:
        return False
