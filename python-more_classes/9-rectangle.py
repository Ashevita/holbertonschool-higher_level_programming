#!/usr/bin/python3
"""Module that defines a Rectangle class"""


class Rectangle:
    """Class that defines a rectangle by its width and height"""

    # Public class attributes
    number_of_instances = 0
    print_symbol = "#"  # Symbol for printing the rectangle

    def __init__(self, width=0, height=0):
        """Initializes the Rectangle with optional width and height.

        Args:
            width (int): The width of the rectangle. Default is 0.
            height (int): The height of the rectangle. Default is 0.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1  # Increment the instance counter

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
        """Defines the string representation of the rectangle
        using the print_symbol.

        Returns:
            str: The string representation of the rectangle.
            If width or height is 0, returns an empty string.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        # Use the class attribute print_symbol to draw the rectangle
        rectangle_str = ""
        for i in range(self.__height):
            rectangle_str += str(self.print_symbol) * self.__width
            if i < self.__height - 1:
                rectangle_str += "\n"  # Newline between rows
        return rectangle_str

    def __repr__(self):
        """Returns a string representation of the rectangle
        to recreate a new instance.

        Returns:
            str: A string in the format "Rectangle(width, height)".
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Prints a message when an instance of Rectangle is deleted
        and decrements the number of instances."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1  # Decrement the instance counter

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Static method that returns the biggest rectangle based on the area.

        Args:
            rect_1 (Rectangle): The first rectangle.
            rect_2 (Rectangle): The second rectangle.

        Returns:
            Rectangle: The rectangle with the greater area.
            Returns rect_1 if both are equal.

        Raises:
            TypeError: If either rect_1 or rect_2
            is not an instance of Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """Class method that returns a new Rectangle
        instance where width == height == size.

        Args:
            size (int): The size of both width and height. Default is 0.

        Returns:
            Rectangle: A new Rectangle instance with equal width and height.
        """
        return cls(size, size)
