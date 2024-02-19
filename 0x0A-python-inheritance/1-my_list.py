#!/usr/bin/python3
"""Program that defines a new class MyList that inherites from list"""


class MyList(list):
    def print_sorted(self):
        """prints the sorted list in ascending order"""
        sorted_list = sorted(self)
        print(sorted_list)
