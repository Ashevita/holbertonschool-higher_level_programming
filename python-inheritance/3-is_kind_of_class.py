#!/usr/bin/python3
"""Module to create class
"""


def is_kind_of_class(obj, a_class):
    """Checks if obj is an instance or inherits from a_class.

    Args:
        obj: The object to check.
        a_class: The class or parent class to compare with.

    Returns:
        True if obj is an instance or subclass instance of a_class,
        False otherwise.
    """
    return isinstance(obj, a_class)
