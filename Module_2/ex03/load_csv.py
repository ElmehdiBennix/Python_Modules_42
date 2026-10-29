"""Load indexed CSV datasets for the projection exercise."""

from pathlib import Path

import pandas as pd


def load(path: str) -> pd.DataFrame | None:
    """Load a CSV file with its first column as the DataFrame index."""
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
        data = pd.read_csv(csv_path, index_col=0)
    except (OSError, UnicodeDecodeError, pd.errors.EmptyDataError,
            pd.errors.ParserError) as error:
        print(f"Error: could not read CSV file: {error}")
        return None

    print(data)

    return data


if __name__ == "__main__":
    print(load("../subject/life_expectancy_years.csv"))
