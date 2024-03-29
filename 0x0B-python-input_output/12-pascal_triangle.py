#!/usr/bin/python3
"""pascals triangle"""


def pascal_triangle(n):
    """pascal triangle"""

    if n <= 0:
        return []

    mylist = []
    for i in range(n):
        value = []
        for j in range(i + 1):
            if j == 0 or j == 1:
                value.append(1)
            else:
                temp = mylist[i - 1]
                value.append(temp[j - 1] + temp[j])
        mylist.append(value)

    return mylist
