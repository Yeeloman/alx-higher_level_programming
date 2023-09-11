#!/usr/bin/python3
"""dds a new attribute"""


def add_attribute(obj, attr, value):
    """add_attribute.

    :param obj:
    :param attr:
    :param value:
    """
    if not hasattr(obj, '__dict__') and not hasattr(obj, '__slots__'):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, attr, value)
