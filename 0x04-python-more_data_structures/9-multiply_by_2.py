#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    keys_copy = list(a_dictionary.keys())
    n_dictionary = {}
    for k in keys_copy:
        for v in a_dictionary:
            n_dictionary[k] = v**2
    return n_dictionary
