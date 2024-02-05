#!/usr/bin/python3
"""basegeometry class module"""


def BaseGeometry():
    """BaseGeometry class"""
    def area(self):
        """Raises exception"""
        raise Exception("area() is not implemented")

def integer_validator(self, name, value):
    """method for validating value"""
    if type(value) != int:
        raise TypeError("{} must be an integer".format(name))
    if value <= 0:
        raise ValueError("{} must be greater than 0".format(name))
