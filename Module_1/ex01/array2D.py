"""Module for slicing and determining dimensions of 2D arrays."""

import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """Slice a 2D array and display its dimensions before and after.

    Args:
        family: A 2D list where all rows must have identical lengths.
        start: Starting slice index (integer).
        end: Ending slice index (integer).

    Returns:
        A truncated 2D list based on start and end slice parameters.
    """

    try:
        if not isinstance(family, list):
            raise TypeError("family must be a list.")

        if not isinstance(start, int) or isinstance(start, bool):
            raise TypeError("start must be an integer.")

        if not isinstance(end, int) or isinstance(end, bool):
            raise TypeError("end must be an integer.")

        if len(family) == 0:
            raise ValueError("family list cannot be empty.")

        row_len = None
        for idx, row in enumerate(family):
            if not isinstance(row, list):
                raise TypeError(f"Element at index {idx} must be a list.")
            if row_len is None:
                row_len = len(row)
            elif len(row) != row_len:
                raise ValueError("All rows must have the same size.")

        arr = np.array(family)
        print(f"My shape is : {arr.shape}")

        sliced_arr = arr[start:end]
        print(f"My new shape is : {sliced_arr.shape}")

        return sliced_arr.tolist()

    except (TypeError, ValueError) as error:
        print(f"Error in slice_me: {error}")
        return []
