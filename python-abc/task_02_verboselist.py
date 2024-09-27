#!/usr/bin/env python3
"""Module to create class
"""


class VerboseList(list):
    """A subclass of list that prints messages when the list is modified."""

    def append(self, item):
        """Appends an item to the list and prints a notification."""
        super().append(item)
        print(f"Added {[item]} to the list.")

    def extend(self, iterable):
        """Extends the list with items from an iterable
        and prints a notification."""
        super().extend(iterable)
        print(f"Extended the list with [{len(iterable)}] items.")

    def remove(self, item):
        """Removes an item from the list and prints a notification."""
        print(f"Removed {[item]} from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """Pops an item from the list and prints a notification."""
        item = self[index]  # Get the item to be popped for the message
        print(f"Popped {[item]} from the list.")
        return super().pop(index)
