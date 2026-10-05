import seaborn as sns
import matplotlib.pyplot as plt
from load_csv import load


def main():
    data = load("../subject/income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    if data is None:
        return

    data2 = load("../subject/life_expectancy_years.csv")
    if data2 is None:
        return

    # Pick a year to compare
    year = "1900"

    # Get GDP and life expectancy for that year
    gdp = data[year]
    life = data2[year]

    # Clean GDP: remove "k" suffix and convert to float
    # "10.3k" -> 10300.0
    gdp = gdp.apply(lambda x: float(str(x).replace("k", "")) * 1000 if "k" in str(x) else float(x))

    # Clean life expectancy: convert to float, drop NaN
    life = life.apply(lambda x: float(x) if str(x).strip() else None)

    # Combine into one DataFrame
    import pandas as pd
    df = pd.DataFrame({"gdp": gdp, "life": life})
    df = df.dropna()

    # Scatter plot
    sns.scatterplot(data=df, x="gdp", y="life")
    plt.title(f"Life Expectancy vs GDP per Capita ({year})")
    plt.xlabel("GDP per capita")
    plt.ylabel("Life Expectancy")
    plt.show()


if __name__ == "__main__":
    main()
