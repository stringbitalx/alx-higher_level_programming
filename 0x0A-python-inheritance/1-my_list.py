#!/usr/bin/python3
"""my list module"""


class MyList(list):
    """Mylist class - inherits from list"""
    def print_sorted(self):
        """prints sorted list"""
        print(sorted(self))
