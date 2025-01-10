from give_bmi import give_bmi
from give_bmi import apply_limit


def main():
    height = [2.71, 1.15, 0]
    weight = [165.3, 38.4, 0]
    result = give_bmi(height, weight)
    print(result, type(result))
    print(apply_limit(result, 26))

    height = [2.71, 1.15]
    weight = [165.3, 38.4]
    result = give_bmi(height, weight)
    print(result, type(result))
    print(apply_limit(result, 26))

    height = [2.71, 1.15, 0]
    weight = [165.3, 38.4, 0]
    result = give_bmi(height, weight)
    print(result, type(result))
    print(apply_limit(result, 26))

    height = ["123", "21314"]
    weight = ["12312", "asdaf"]
    result = give_bmi(height, weight)
    print(result, type(result))
    print(apply_limit(["123", "21314"], 26))

    height = []
    weight = []
    result = give_bmi(height, weight)
    print(result, type(result))
    print(apply_limit([], 26))

    height = "asd"
    weight = "asd"
    result = give_bmi(height, weight)
    print(result, type(result))
    print(apply_limit([], 26))
    return


if __name__ == "__main__":
    main()
