#!/usr/bin/python3


def say_my_name(first_name, last_name=""):
    """say_my_name.

    Args:
        param first_name: first name.
        param last_name: last_name.
    """
    if not first_name or not isinstance(first_name, str) or not first_name.strip():
        raise TypeError("first_name must be a string")
    if last_name == None or not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
