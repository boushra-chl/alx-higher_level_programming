#!/usr/bin/python3
"""creates an Object from a JSON file"""


def load_from_json_file(filename):
    """function that creates an Object from a “JSON file”"""
    import json
    with open(filename, encoding="utf-8") as f:
        my_obj = json.load(f)
    f.close()
    return my_obj
