from ft_filter import ft_filter
import sys


def main():
    lst_arg = sys.argv
    try:
        assert len(lst_arg) == 3, "AssertionError: the arguments are bad"
        flag = True
        try:
            arg = int(lst_arg[2])
        except ValueError:
            flag = False
        assert flag, "AssertionError: the arguments are bad"
    except AssertionError as msg:
        print(msg)
        return
    string = lst_arg[1]
    lst = string.split(" ")
    it = ft_filter(lambda x: len(x) == arg, lst)
    print(list(it))
    return


if __name__ == "__main__":
    main()
