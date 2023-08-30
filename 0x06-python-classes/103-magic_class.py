#!/usr/bin/python3

import math


class MagicClass:
    """MagicClass class"""
    def __init__(self, radius):
        """
        Initialize a MagicClass instance.

        Args:
            radius (int or float): The radius of the circle.

        Raises:
            TypeError: If radius is not an int or float.
        """
        self._MagicClass__radius = 0

        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self._MagicClass__radius = radius

    def area(self):
        """
        Calculate the area of a circle.

        Returns:
            float: The calculated area.
        """
        return self._MagicClass__radius ** 2 * math.pi

    def circumference(self):
        """
        Calculate the circumference of a circle.

        Returns:
            float: The calculated circumference.
        """
        return 2 * math.pi * self._MagicClass__radius
