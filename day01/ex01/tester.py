from array2D import slice_me


def main():
    family = [
                [1.80, 78.4],
                [2.15, 102.7],
                [2.10, 98.5],
                [1.88, 75.2]
            ]

    print(slice_me(family, 0, 2))
    print("test1")
    print(slice_me(family, 1, -2))
    print("test2")
    print(slice_me(family, 3, 2))
    print("test3")
    print(slice_me(family, 0, 0))
    print("test4")
    print(slice_me(family, -3, -2))
    print("test5")
    print(slice_me(family, "sd", "dsa"))
    print("test6")
    print(slice_me([[]], 0, 2))
    return


if __name__ == "__main__":
    main()
