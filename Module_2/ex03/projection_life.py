"""Plot life expectancy against income for a selected year."""

import matplotlib.pyplot as plt
import pandas as pd

from load_csv import load


def main():
    """Plot life expectancy against income for the year 1900."""
    try:
        income_path = "../subject/"
        income_file = (
            "income_per_person_gdppercapita_ppp_"
            "inflation_adjusted.csv"
        )
        income_path += income_file
        data = load(income_path)
        if data is None:
            return

        life_path = "../subject/life_expectancy_years.csv"
        data2 = load(life_path)
        if data2 is None:
            return

        year = "1900"
        if year not in data.columns or year not in data2.columns:
            print(f"Error: year {year} was not found in both datasets")
            return

        gdp = data[year]
        life = data2[year]

        gdp = gdp.apply(
            lambda x: (
                float(str(x).replace("k", "")) * 1000
                if "k" in str(x)
                else float(x)
            )
        )
        life = life.apply(lambda x: float(x) if str(x).strip() else None)

        df = pd.DataFrame({"gdp": gdp, "life": life}).dropna()
        if df.empty:
            print("Error: no complete data points were found for 1900")
            return

        plt.scatter(df["gdp"], df["life"], label="Countries")
        plt.title(f"Life Expectancy vs GDP per Capita ({year})")
        plt.xlabel("GDP per capita")
        plt.ylabel("Life Expectancy")
        plt.legend()
        plt.show()
    except (KeyError, TypeError, ValueError, OSError) as error:
        print(f"Error: could not plot projection data: {error}")


if __name__ == "__main__":
    main()
