"""Identify and print Python's null-like values."""

from typing import Any


def NULL_not_found(object: Any) -> int:
    """Print the label of a null-like value and return 0 or 1."""
    if object is None:
        print(f"Nothing: {object} {type(object)}")
        return 0
    if type(object) is bool and object is False:
        print(f"Fake: {object} {type(object)}")
        return 0
    if type(object) is int and object == 0:
        print(f"Zero: {object} {type(object)}")
        return 0
    if type(object) is float and object != object:
        print(f"Cheese: {object} {type(object)}")
        return 0
    if type(object) is str and object == "":
        print(f"Empty: {type(object)}")
        return 0
    print("Type not Found")
    return 1
