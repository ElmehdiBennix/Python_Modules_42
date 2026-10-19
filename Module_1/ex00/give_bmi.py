"""Module for calculating BMI and applying threshold limits."""

from decimal import DivisionByZero

import numpy as np


def give_bmi(
    height: list[int | float], weight: list[int | float]
) -> list[int | float]:
    """Calculate the Body Mass Index (BMI) for paired height and weight values.

    Formula used: weight / (height ** 2).

    Args:
        height: List of heights in meters (must be positive numbers).
        weight: List of weights in kilograms (must be positive numbers).

    Returns:
        A list of calculated BMI values as floats, or an empty list on error.
    """
    try:
        if not isinstance(height, list) or not isinstance(weight, list):
            raise TypeError("Both height and weight must be list types.")

        if len(height) != len(weight):
            raise ValueError(
                "Height and weight lists must have the same size.")

        if len(height) == 0:
            raise ValueError("Lists cannot be empty.")

        for h, w in zip(height, weight):
            if not isinstance(h, (int, float)) or isinstance(h, bool):
                raise TypeError("Height elements must be int or float.")
            if not isinstance(w, (int, float)) or isinstance(w, bool):
                raise TypeError("Weight elements must be int or float.")
            if h <= 0 or w <= 0:
                raise ValueError(
                    "Height and weight must be greater than zero.")

        h_arr = np.array(height, dtype=float)
        w_arr = np.array(weight, dtype=float)

        bmi_results = w_arr / (h_arr**2)
        return bmi_results.tolist()

    except (TypeError, ValueError, DivisionByZero) as error:
        print(f"Error in give_bmi: {error}")
        return []


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Check which BMI values strictly exceed a specified threshold limit.

    Args:
        bmi: List of BMI values (ints or floats).
        limit: Integer threshold to compare against.

    Returns:
        A list of booleans where True means the BMI exceeds the limit.
    """
    try:
        if not isinstance(bmi, list):
            raise TypeError("The bmi argument must be a list.")

        if not isinstance(limit, int) or isinstance(limit, bool):
            raise TypeError("The limit argument must be an integer.")

        for val in bmi:
            if not isinstance(val, (int, float)) or isinstance(val, bool):
                raise TypeError("All BMI elements must be int or float.")

        bmi_arr = np.array(bmi, dtype=float)
        limit_results = bmi_arr > limit

        return limit_results.tolist()

    except (TypeError, ValueError) as error:
        print(f"Error in apply_limit: {error}")
        return []
