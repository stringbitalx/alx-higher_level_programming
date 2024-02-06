#!/usr/bin/python3
"""create python obj from json file"""


def load_from_json_file(filename):
    """creates python obj from json file"""

    with open(filename) as file:
        return json.load(file)
