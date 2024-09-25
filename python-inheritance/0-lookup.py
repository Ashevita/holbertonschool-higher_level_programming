#!/usr/bin/python3
"""Module to create class
"""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.

    Args:
        obj: The object whose attributes and methods will be returned.

    Returns:
        A list of strings representing the names
        of the attributes and methods available for the object.
    """
    return dir(obj)
