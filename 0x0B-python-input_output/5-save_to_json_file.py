#!/usr/bin/python3
"""writes an obj to text file using json representation"""


def save_to_json_file(my_obj, filename):
    """writes obj to txt file using json representation"""

    with open(filenmae, mode="w") as file:
        json.dump(my_obj, file)
