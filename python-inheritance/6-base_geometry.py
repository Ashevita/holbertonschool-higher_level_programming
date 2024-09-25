#!/usr/bin/python3
"""Module to create class
"""


class BaseGeometry:
    """A base class for geometry with an unimplemented area method.
    """

    def area(self):
        """Calculates the area of the geometry.

        Raises:
            Exception: If the area method is not implemented.
        """
        raise Exception("area() is not implemented")
