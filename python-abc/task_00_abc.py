#!/usr/bin/env python3
"""Module to create class
"""


from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract class for animals."""

    @abstractmethod
    def sound(self):
        """Returns the animal sound."""
        pass


class Dog(Animal):
    """Represents a dog."""

    def sound(self):
        """Returns 'Bark'."""
        return "Bark"


class Cat(Animal):
    """Represents a cat."""

    def sound(self):
        """Returns 'Meow'."""
        return "Meow"
