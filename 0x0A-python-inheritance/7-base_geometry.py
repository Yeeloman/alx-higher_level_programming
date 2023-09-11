#!/usr/bin/python3


class BaseGeometry:
    """BaseGeometry."""

    def area(self):
        """area."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """integer_validator.

        :param name:
        :param value:
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
