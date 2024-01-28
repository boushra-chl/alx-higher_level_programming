#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    keys_copy = list(a_dictionary.keys())
    for k in keys_copy:
        if k == key:
            del a_dictionary[k]
    return a_dictionary
