#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    keys_copy = list(a_dictionary.keys())
    for k in keys_copy:
        if key == k:
            a_dictionary[k] = value
        else:
            a_dictionary[key] = value
    return a_dictionary
