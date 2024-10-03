#!/usr/bin/python3
"""Module to create class
"""


def read_file(filename=""):
    """Reads a file and prints its content."""
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
    print(content, end="")
