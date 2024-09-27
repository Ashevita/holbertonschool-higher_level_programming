#!/usr/bin/env python3
"""Classes Fish, Bird et FlyingFish."""


class SwimMixin:
    """Mixin that provides swimming ability."""
    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """Mixin that provides flying ability."""
    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """A dragon that can swim, fly, and roar."""
    def roar(self):
        """Method for dragon's roar."""
        print("The dragon roars!")
