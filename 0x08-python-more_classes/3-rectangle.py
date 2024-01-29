#!/usr/bin/python3
"""defines a squaere base on 2-square.py"""


class Square:
    """square"""

    def __init__(self, size=0):
        """init the data"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("Size must be >= 0")
        self.__size = size

        def area(size):
            """return the current square area"""

            return (self.__size * self.__size)
