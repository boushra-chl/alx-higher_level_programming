#!/usr/bin/python3
"""module that reads a file"""


def read_file(filename=""):
    """function that reads from file"""
    with open(filename, encoding="utf-8") as f:
        read_txt = f.read()
    print(read_txt, end="")
    f.close()
