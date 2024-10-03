#!/usr/bin/python3
"""Module to deserialize JSON strings."""


import json


def from_json_string(my_str):
    """Deserializes a JSON string to a Python object.

    Args:
        my_str (str): The JSON string to deserialize.

    Returns:
        The corresponding Python object.
    """
    return json.loads(my_str)
