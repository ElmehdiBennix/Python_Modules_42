from logging import exception
from pathlib import Path

import pandas as pd
from pandas.core.frame import DataFrame


def load(path: str) -> DataFrame | None:
    csv_path = Path(path)

    if not csv_path.is_file():
        print("1")
        return None

    if csv_path.suffix != ".csv":
        print("2")
        return None

    try:
        data = pd.read_csv(csv_path, index_col=0)
    except Exception as e:
        print("3")
        return None

    print(data)

    return data


if __name__ == "__main__":
    print(load("../subject/life_expectancy_years.csv"))
