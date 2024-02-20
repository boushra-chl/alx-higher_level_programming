#!/usr/bin/python3
"""module that serialises an oject"""


def to_json_string(my_obj):
    """function that returns the JSON representation of an object (string)"""
    import json
    serialised = json.dumps(my_obj)
    return serialised
