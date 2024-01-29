#!/usr/bin/python3
"""defines a square bassed on 1-square.py"""


class Square:
    """Square"""

    def __init__(self, size=0):
        """init the data"""


        self.__size = size

    @property
    def size(self):
        """return size of square"""
        return self.__size

    def area(self):
        """return the current square area"""

        return (self.__size * self.__size)

    @size.setter
    def size(self, value):
        """sets size"""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >=0")
        self.__size = value
