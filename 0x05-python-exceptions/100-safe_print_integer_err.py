#!/usr/bin/python3
import sys
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        res = True
    except ValueError:
        print("Exception: Unknown format code \'d\' for object of type \'str\'", file=sys.stderr)
        res = False
    return res
