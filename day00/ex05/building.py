import sys


def main():
    try:
        lst_arg = sys.argv
        AssErr = "AssertionError: more than one argument is provided"
        assert len(lst_arg) <= 2, AssErr
    except AssertionError as msg:
        print(msg)
        return
    if (len(lst_arg) < 2 or not lst_arg[1]):
        string = ""
        try:
            while not string:
                string = input("What is the text to count?\n")
        except EOFError:
            print("the input is still empty")
            return
    else:
        string = lst_arg[1]
    nbCharacters = sum(1 for c in string if c.isprintable())
    nbSpace = sum(1 for c in string if c.isspace())
    nbDigit = sum(1 for c in string if c.isdigit())
    nbLetter = sum(1 for c in string if c.isalpha())
    nbPonctuation = nbCharacters - nbSpace - nbDigit - nbLetter
    print("The text contains %d characters" % nbCharacters)
    print("%d upper letters" % sum(1 for c in string if c.isupper()))
    print("%d lower letters" % sum(1 for c in string if c.islower()))
    print("%d punctuation marks" % nbPonctuation)
    print("%d spaces" % nbSpace)
    print("%d digits" % nbDigit)
    string.count


if __name__ == "__main__":
    main()
