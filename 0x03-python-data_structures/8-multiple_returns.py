#!/usr/bin/python3
def multiple_returns(sentence):
    len_tuple = len(sentence)
    if sentence == "":
        first_char = None
    else:
        first_char = sentence[0]
    rs_tuple = (len_tuple, first_char)
    return rs_tuple
