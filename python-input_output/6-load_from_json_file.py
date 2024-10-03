#!/usr/bin/python3
"""Module to create class
"""


import json


def load_from_json_file(filename):
    """Creates an object from a JSON file."""
    with open(filename, "r", encoding='UTF-8') as f:
        return json.load(f)
