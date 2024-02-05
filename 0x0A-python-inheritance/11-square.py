#!/usr/bin/python3
"""square class module"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """square class"""
    def __init__(self, size):
        """initialize square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """returns area of square"""
        return self.__square ** 2

    def __str__(self):
        """Returns a string"""
        return "[square] {}/{}".format(self.__size, self.__size)
