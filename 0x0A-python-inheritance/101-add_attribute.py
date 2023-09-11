#!/usr/bin/python3
"""dds a new attribute"""


def add_attribute(obj, attr, value):
    """add_attribute.

    :param obj:
    :param attr:
    :param value:
    """
    if '__dict__' not in dir(obj):
        raise TypeError("can't add new attr")
    if '__slots__' in dir(obj):
        raise TypeError("can't add new attr")
    else:
        setattr(obj, attr, value)
