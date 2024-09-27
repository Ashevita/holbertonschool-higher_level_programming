#!/usr/bin/env python3
"""Module to create class
"""


from abc import ABC, abstractmethod
import math


class Shape(ABC):

    """Classe abstraite pour les formes géométriques."""
    @abstractmethod
    def area(self):
        """Retourne l'aire de la forme."""
        pass

    @abstractmethod
    def perimeter(self):
        """Retourne le périmètre de la forme."""
        pass


class Circle(Shape):
    """Représente un cercle avec un rayon donné."""

    def __init__(self, radius):
        """Initialise le cercle avec un rayon."""

        self.radius = radius

    def area(self):

        """Calcule l'aire du cercle."""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Calcule le périmètre du cercle."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Représente un rectangle avec une largeur et une hauteur."""

    def __init__(self, width, height):
        """Initialise le rectangle avec une largeur et une hauteur."""
        self.width = width
        self.height = height

    def area(self):
        """Calcule l'aire du rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Calcule le périmètre du rectangle."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Affiche l'aire et le périmètre de la forme."""
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
