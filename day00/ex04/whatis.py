import sys

lst_arg = sys.argv
if (len(lst_arg) > 1):
    try:
        assert len(lst_arg) == 2, "AssertionError: \
more than one argument is provided"
        try:
            arg = int(lst_arg[1])
            if arg % 2 == 0:
                print("I'm Even.")
            else:
                print("I'm Odd.")
        except ValueError:
            raise AssertionError("AssertionError: argument is not an integer")
    except AssertionError as msg:
        print(msg)
