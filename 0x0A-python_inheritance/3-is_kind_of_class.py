#!/usr/bin/python3
"""checks if obj is an instance"""


def is_kind_of_class(obj, a_class):
    """function that returns true ifobj is an instrance"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
