import matplotlib.pyplot as plt
import pandas as pd
from load_csv import load


def main():
    data = load("../subject/life_expectancy_years.csv")
    if data is None:
        return

    print(data)

    france = data.loc["France"]

    plt.plot(france.index, france.values)
    plt.xticks(france.index[::40])
    plt.tight_layout()
    plt.xlabel("Year")
    plt.ylabel("Life expectancy")
    plt.title("France Life expectancy Projections")
    plt.show()

main()
