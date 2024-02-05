#!/usr/bin/python3
"""method inherits_from"""


def inherits_from(obj, a_class):
    """returns true if obj is an instance of a class that
    inherited directly/indirectly from specified class
    o/w false"""
    return isinstance(obj, a_class) and type(obj) != a_class
