import matplotlib.pyplot as plt
import pandas as pd
from load_csv import load
import numpy as np

def replaceChar(value: str):
    if (value.find("B") > 0):
        return float(value.replace('B', '')) * 1000000000
    if (value.find("M") > 0):
        return float(value.replace('M', '')) * 1000000
    if (value.find("k") > 0):
        return float(value.replace('K', '')) * 1000
    return float(value)

def replaceSeries(value: pd.Series):
    return value.transform(lambda x: replaceChar(x))


def main():
    data = load("population_total.csv")
    print(data.head())
    year = [str(year) for year in range(1800, 2051)]
    popFr = data[data['country'] == "France"]
    popBl = data[data['country'] == "Belgium"]
    popFr = popFr[year].values.flatten() #transform en numpy table
    popBl = popBl[year].values.flatten()
    popFr = [replaceChar(pop) for pop in popFr]
    popBl = [replaceChar(pop) for pop in popBl]
    plt.plot(year, popFr)
    plt.plot(year, popBl)
    plt.ylabel('Population')
    plt.xlabel('Year')
    plt.legend(("Belgium", "France"),  loc='lower right')
    plt.title("Population Projections")
    plt.xticks(year[::40])

    max_pop = max(max(popFr), max(popBl))
    if max_pop > 1e9:
        y_ticks = [i * 1e9 for i in range(0, int(max_pop / 1e9) + 1, 2)]
        plt.yticks(
            y_ticks, ["{:,.0f}B".format(pop / 1e9) for pop in y_ticks])
    elif max_pop > 1e6:
        y_ticks = [i * 1e7 for i in range(0, int(max_pop / 1e7) + 1, 2)]
        plt.yticks(
            y_ticks, ["{:,.0f}M".format(pop / 1e6) for pop in y_ticks])
    else:
        y_ticks = [i * 1e3 for i in range(0, int(max_pop / 1e3) + 1, 2)]
        plt.yticks(
            y_ticks, ["{:,.0f}K".format(pop / 1e3) for pop in y_ticks])
    plt.show()
    return


if __name__ == "__main__":
    main()
