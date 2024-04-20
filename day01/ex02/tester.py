from load_image import ft_load


def main():
    print(ft_load("landscape.jpg"))
    ft_load("landscape.png")
    print(ft_load("tester.py"))
    print(ft_load(12))
    print(ft_load(""))
    return


if __name__ == "__main__":
    main()
