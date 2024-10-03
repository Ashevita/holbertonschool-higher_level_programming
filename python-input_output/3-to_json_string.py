#!/usr/bin/python3
"""Module to serialize Python objects to JSON."""


import json


def to_json_string(my_obj):

    """Serializes a Python object to a JSON string.

    Args:
        my_obj: The Python object to serialize.

    Returns:
        str: The JSON string representation of the object.
    """
    return json.dumps(my_obj)
