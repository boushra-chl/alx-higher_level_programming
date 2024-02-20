#!/usr/bin/python3
"""module that writes to a file"""
def write_file(filename="", text=""):
    """function that writes to a string to a text file (UTF8) and returns
    the number of characters written"""


    with open(filename, "w", encoding="utf-8") as f:
        characters = f.write(text)
    f.close()
    return characters
