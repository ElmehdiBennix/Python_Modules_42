"""Print the type of an object and return 42."""

from typing import Any


def all_thing_is_obj(object: Any) -> int:
    """Print a label for the object's type and return 42."""
    labels = {list: "List", tuple: "Tuple", set: "Set", dict: "Dict"}
    label = labels.get(type(object))
    if label is not None:
        print(f"{label} : {type(object)}")
    elif type(object) is str:
        print(f"{object} is in the kitchen : {type(object)}")
    else:
        print("Type not found")
    return 42
