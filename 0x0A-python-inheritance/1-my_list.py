#!/usr/bin/python3
"""Contains the MyList class."""


class MyList(list):
    """a subclass of list"""

    def print_sorted(self):
        """prints the sorted list"""
        print(sorted(self))
