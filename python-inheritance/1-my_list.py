#!/usr/bin/python3
"""Module to create class
"""


class MyList(list):
    """A subclass of list that can print a sorted version of itself."""

    def print_sorted(self):
        """Prints the list in sorted (ascending) order."""
        print(sorted(self))
