#!/usr/bin/python3
"""Module that defines a Rectangle class"""


class Rectangle:
    """Class that defines a rectangle by its width and height"""

    def __init__(self, width=0, height=0):
        """Initializes the Rectangle with optional width and height.

        Args:
            width (int): The width of the rectangle. Default is 0.
            height (int): The height of the rectangle. Default is 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter method to retrieve the width of the rectangle.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method to set the width of the rectangle.

        Args:
            value (int): The new width value.

        Raises:
            TypeError: If the width is not an integer.
            ValueError: If the width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter method to retrieve the height of the rectangle.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method to set the height of the rectangle.

        Args:
            value (int): The new height value.

        Raises:
            TypeError: If the height is not an integer.
            ValueError: If the height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates the area of the rectangle.

        Returns:
            int: The area of the rectangle (width * height).
        """
        return self.__width * self.__height

    def perimeter(self):
        """Calculates the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle, or 0 if width or height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Defines the string representation of the
        rectangle using the '#' character.

        Returns:
            str: The string representation of the rectangle.
            If width or height is 0, returns an empty string.
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        rectangle_str = ""
        for i in range(self.__height):
            rectangle_str += "#" * self.__width
            if i < self.__height - 1:
                rectangle_str += "\n"
        return rectangle_str

    def __repr__(self):
        """Returns a string representation of the
        rectangle to recreate a new instance.

        Returns:
            str: A string in the format "Rectangle(width, height)".
        """
        return f"Rectangle({self.__width}, {self.__height})"
