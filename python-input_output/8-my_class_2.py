#!/usr/bin/python3
"""Module for MyClass."""


class MyClass:
    """Represents a class with a name, number, and score."""

    score = 0

    def __init__(self, name, number=4):
        """Initializes MyClass with a name and an optional number."""
        self.__name = name
        self.number = number
        self.is_team_red = (self.number % 2) == 0

    def win(self):
        """Increments the score by 1."""
        self.score += 1

    def lose(self):
        """Decrements the score by 1."""
        self.score -= 1

    def __str__(self):
        """Returns a string representation of MyClass."""
        return (
            "[MyClass] {} - {} => {}".format(
                self.__name,
                self.number,
                self.score
            )
        )
