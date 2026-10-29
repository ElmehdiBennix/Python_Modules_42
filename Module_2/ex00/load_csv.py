"""Load CSV datasets for the first DataTable exercise."""

from pathlib import Path

import pandas as pd


def load(path: str):
    """Load a CSV file, print its dimensions, and return its DataFrame."""
    if not isinstance(path, str):
        print("Error: path must be a string")
        return None

    csv_path = Path(path)

    if not csv_path.is_file():
        print(f"Error: file not found: {path}")
        return None

    if csv_path.suffix.lower() != ".csv":
        print("Error: file must have a .csv extension")
        return None

    try:
        data = pd.read_csv(csv_path)
    except (OSError, UnicodeDecodeError, pd.errors.EmptyDataError,
            pd.errors.ParserError) as error:
        print(f"Error: could not read CSV file: {error}")
        return None

    print(f"Loading dataset of dimensions {data.shape}")
    return data


if __name__ == "__main__":
    print(load("../subject/life_expectancy_years.csv"))
