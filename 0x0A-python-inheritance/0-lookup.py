#!/usr/bin/python3
"""Defines an object attributes lookup function"""


def lookup(obj):
    """Return a list of attributes and methods"""
    return (dir(obj))
