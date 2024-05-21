import matplotlib.pyplot as plt
import matplotlib.scale as scl
import pandas as pd
from load_csv import load


def main():
    incomeData = load(
        "income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    lifeExpectationData = load("life_expectancy_years.csv")
    if (not isinstance(incomeData, pd.DataFrame) or
            not isinstance(lifeExpectationData, pd.DataFrame)):
        return
    incomeData = incomeData["1900"]
    lifeExpectationData = lifeExpectationData["1900"]
    plt.scatter(incomeData, lifeExpectationData)
    plt.xlabel("Gross domestic product")
    plt.ylabel("Life Expectancy")
    plt.title("1900")
    plt.xscale(scl.LogScale(axis="x"))
    plt.xticks([300, 1000, 10000], ["300", "1k", "10k"])
    plt.show()
    return


if __name__ == "__main__":
    main()
