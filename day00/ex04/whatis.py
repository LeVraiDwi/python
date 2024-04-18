import sys

lst_arg = sys.argv
try:
    assert len(lst_arg) == 2, "AssertionError: more than one argument is provided"
    flag = True
    try:
        arg = int(lst_arg[1])
    except ValueError:
        flag = False
    assert flag, "AssertionError: argument is not an integer"
    arg = int(lst_arg[1])
    if arg % 2 == 0:
        print("I'm Even")
    else:
        print("I'm Odd")
except AssertionError as msg: 
    print(msg)
    
