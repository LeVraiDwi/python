from load_csv import load


def main():
    print(load("life_expectancy_years.csv"))
    load(1)
    load(".csv")
    print(load("tester.py"))
    print(load(""))
    return


if __name__ == "__main__":
    main()
