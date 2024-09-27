#!/usr/bin/env python3
"""CountedIterator class."""


class CountedIterator:
    """Iterator with a counter."""

    def __init__(self, iterable):
        """Initialization."""
        self.iterator = iter(iterable)
        self.count = 0

    def __next__(self):
        """Returns the next item."""
        item = next(self.iterator)
        self.count += 1
        return item

    def get_count(self):
        """Returns the number of items iterated."""
        return self.count
