#!/usr/bin/python3
"""module that returns an object represented by a JSON string"""


def from_json_string(my_str):
    """ function that returns an object (Python data structure)
    represented by a JSON string"""
    import json
    deserialised = json.loads(my_str)
    return deserialised
