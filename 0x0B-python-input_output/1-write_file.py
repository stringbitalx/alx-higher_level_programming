#!/usr/bin/python3
"""write file function"""


def write_file(filename="", text=""):
    """writes string to file and returns no of chars written"""

    with open(filename, mode="w", encoding="utf-8") as file:
        return (file.write(text))
