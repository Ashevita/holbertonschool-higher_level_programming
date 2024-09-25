#!/usr/bin/python3
"""Module to create class
"""


class BaseGeometry:

    """A base class for geometry with methods for area
    calculation and validation.
    """

    def area(self):
        """Calculates the area of the geometry.

        Raises:
            Exception: If the area method is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that value is a positive integer.

        Args:
            name (str): The name of the parameter being validated.
            value (int): The value to be validated.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):

    """A class representing a rectangle that inherits from BaseGeometry.
    """

    def __init__(self, width, height):
        """Instantiation of a rectangle with width and height.

        Validates width and height using integer_validator.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculates the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """Returns the string representation of the rectangle.

        Returns:
            str: A description of the rectangle.
        """
        return f"[Rectangle] {self.__width}/{self.__height}"


class Square(Rectangle):

    """A class representing a square that inherits from Rectangle.
    """

    def __init__(self, size):
        """Instantiation of a square with a given size.

        Validates size using integer_validator.

        Args:
            size (int): The size of the square's sides.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size

    def __str__(self):
        """Returns the string representation of the square.

        Returns:
            str: A description of the square.
        """
        return f"[Square] {self.__size}/{self.__size}"
