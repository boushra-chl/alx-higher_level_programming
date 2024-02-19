#!/usr/bin/python3
"""This module inherites from the list class"""


class MyList(list):
    def print_sorted(self):
        """prints the sorted list in ascending order"""
        sorted_list = sorted(self)
        print(sorted_list)
