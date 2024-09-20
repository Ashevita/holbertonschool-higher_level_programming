#!/usr/bin/python3
"""Module that defines a Rectangle class"""


class Rectangle:
    """Class that defines a rectangle by its width and height."""

    # Public class attributes
    number_of_instances = 0  # To track the number of instances
    print_symbol = "#"       # Symbol used for string representation

    def __init__(self, width=0, height=0):
        """Initializes the Rectangle with optional width and height."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1  # Increment the instance counter

    @property
    def width(self):
        """Getter method to retrieve the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method to set the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter method to retrieve the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method to set the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Public instance method that returns the rectangle area."""
        return self.__width * self.__height

    def perimeter(self):
        """Public instance method that returns the rectangle perimeter.
        If either width or height is 0, the perimeter is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """String representation of the rectangle with the print_symbol.
        If width or height is 0, returns an empty string.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle_str = (
            (str(self.print_symbol) * self.__width + "\n") * self.__height
        )
        return rectangle_str.rstrip()  # Remove the last newline

    def __repr__(self):
        """Return a string representation of the rectangle to be able to
        recreate a new instance by using eval().
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Print a message when an instance of Rectangle is deleted and
        decrement the number of instances.
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
