import matplotlib.pyplot as plt
from load_csv import load
from matplotlib.ticker import FuncFormatter


def main():
    data = load("../subject/population_total.csv")
    if data is None:
        return

    france = data.loc["France"]
    belgium = data.loc["Belgium"]

    # Convert "29M" → 29000000, "3.25M" → 3250000
    france = france.apply(lambda x: float(x.replace("M", "")) * 1e6)
    belgium = belgium.apply(lambda x: float(x.replace("M", "")) * 1e6)

    # Filter years 1800-2050
    years = france.index[(france.index >= "1800") & (france.index <= "2050")]
    france = france[years]
    belgium = belgium[years]

    plt.plot(belgium.index, belgium.values, label="Belgium", color="blue")
    plt.plot(france.index, france.values, label="France", color="green")

    plt.title("Population Projections")
    plt.xlabel("Year")
    plt.ylabel("Population")

    # Format y-axis as 20M, 40M, 60M
    ax = plt.gca()
    ax.yaxis.set_major_formatter(FuncFormatter(lambda x, p: f"{int(x / 1e6)}M"))
    plt.yticks([0, 20000000, 40000000, 60000000])

    plt.xticks(france.index[::20], rotation=45)
    plt.legend(loc="lower right")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
