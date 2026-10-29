"""Plot France's life expectancy from the DataTable dataset."""

import matplotlib.pyplot as plt

from load_csv import load


def main():
    """Plot France's life expectancy over time."""
    try:
        data = load("../subject/life_expectancy_years.csv")
        if data is None:
            return

        print(data)
        if "France" not in data.index:
            print("Error: country 'France' was not found")
            return

        france = data.loc["France"]
        plt.plot(france.index, france.values)
        plt.xticks(france.index[::40])
        plt.tight_layout()
        plt.xlabel("Year")
        plt.ylabel("Life expectancy")
        plt.title("France Life expectancy Projections")
        plt.show()
    except (KeyError, TypeError, ValueError, OSError) as error:
        print(f"Error: could not plot life expectancy data: {error}")


if __name__ == "__main__":
    main()
