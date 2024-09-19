#!/usr/bin/python3
"""Module to create class
"""


class Square:
    """A class that defines a square by its size."""
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """Getter for the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Initialize the square with a private size attribute."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size * self.__size
