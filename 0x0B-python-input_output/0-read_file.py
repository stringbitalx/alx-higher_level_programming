#!/usr/bin/python3
"""read file function"""


def read_file(filename=""):
    """read file content and prints a line at a time"""

    with open(filename, mode="r", encoding="utf-8") as file:
        for line in file:
            print(line, end="")
