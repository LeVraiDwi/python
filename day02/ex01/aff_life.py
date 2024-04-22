import matplotlib.pyplot as plt
import pandas as pd
from load_csv import load
import numpy as np



def main():
    data = load("life_expectancy_years.csv")
    print(data.head())
    france = data[data["country"] == "France"]
    print(france)
    france = france.iloc[: , 1:]
    france.rename({1800: 1840}, axis="index")
    print(france)
    france = france.transpose()
    france.plot()
    plt.ylabel('life expectancy')
    plt.xlabel('Year')
    plt.legend().remove()
    plt.title("France Life expectancy Projections")
    plt.xticks(np.arange(0, 300, 40), np.arange(1800, 2100, 40))
    plt.show()
    return


if __name__ == "__main__":
    main()
