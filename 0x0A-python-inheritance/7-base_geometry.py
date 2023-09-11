#!/usr/bin/python3
"""class"""


class BaseGeometry:
    """BaseGeometry."""

    def area(self):
        """area."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """integer_validator.

        :param name: name.
        :param value: value.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
