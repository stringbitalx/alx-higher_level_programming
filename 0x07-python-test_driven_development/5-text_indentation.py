#!/usr/bin/python3
"""prints 2 new lines after . : an ?"""


def tex_identation(text):
    """prints 2 new lines after . : and ?"""

    if type(text) is not str:
        raise TypeError("text must be a string")

    s = text[:]

    for d in ".:?":
        list_text = s.split(d)
        s = ""
        for i in list_text:
            i = i.strip(" ")
            s = i + d if s is ""else s + "\n\n" + i + d

    print(s[:-3], end ="")
