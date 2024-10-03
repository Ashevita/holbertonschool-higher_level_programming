#!/usr/bin/python3
"""Module to create class
"""


def class_to_json(obj):
    """Returns the dictionary description
      for JSON serialization of an object."""
    return obj.__dict__
