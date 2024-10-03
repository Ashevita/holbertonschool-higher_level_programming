#!/usr/bin/python3
"""Module for MyClass."""


class MyClass:
    """Defines a class with a name and a number."""

    def __init__(self, name):
        """Initializes MyClass with a name and sets number to 0."""
        self.name = name
        self.number = 0

    def __str__(self):
        """Returns a string representation of MyClass."""
        return "[MyClass] {} - {:d}".format(self.name, self.number)
