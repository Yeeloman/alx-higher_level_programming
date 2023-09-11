#!/usr/bin/python3
"""dds a new attribute"""


def can_add_attribute(obj):
    """Check if an object allows dynamic attribute assignment."""
    return hasattr(obj, '__dict__') or hasattr(type(obj), '__dict__')


def add_attribute(obj, attribute, value):
    """Adds a new attribute to an object if it's possible."""
    if can_add_attribute(obj):
        setattr(obj, attribute, value)
    else:
        raise TypeError("can't add new attribute")
