#!/usr/bin/python3
"""defines a rectangle"""


class Rectangle:
    """a class rectangle that defines a rectangle"""
    def __init__(self, width=0, height=0):
        """init width & height"""

        self.width = width
        self.height = height

    @property
    def width(self):
        """self with attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """set width attribute"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >=0")

        self.__width = value

    @property
    def height(self):
        """set height attribute"""

        return self.__height

    @height.setter
    def height(self, value):
        """set new height attribure"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >=0")

        self.__height = value
