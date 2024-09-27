#!/usr/bin/env python3
"""Module to create class
"""

class VerboseList(list):
    def append(self, item):
        super().append(item)
        print(f"Added [{item}] to the list.")
    def extend(self, item):
