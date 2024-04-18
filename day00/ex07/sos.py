import sys


def main():
    lst_arg = sys.argv
    try:
        assert len(lst_arg) == 2, "AssertionError: the arguments are bad"
        n = sum(1 for c in lst_arg[1] if not c.isalnum() and not c.isspace())
        assert n == 0, "AssertionError: the arguments are bad"
    except AssertionError as msg:
        print(msg)
        return

    NESTED_MORSE = {" ": "/ ",
                    "A": ".- ",
                    "B": "-... ",
                    "C": "-.-. ",
                    "D": "-.. ",
                    "E": ". ",
                    "F": "..-. ",
                    "G": "--. ",
                    "H": ".... ",
                    "I": ".. ",
                    "J": ".--- ",
                    "K": "-.- ",
                    "L": ".-.. ",
                    "M": "-- ",
                    "N": "-. ",
                    "O": "--- ",
                    "P": ".--. ",
                    "Q": "--.- ",
                    "R": ".-. ",
                    "S": "... ",
                    "T": "- ",
                    "U": "..- ",
                    "V": "...- ",
                    "W": ".-- ",
                    "X": "-..- ",
                    "Y": "-.-- ",
                    "Z": "--.. ",
                    "1": ".---- ",
                    "2": "..--- ",
                    "3": "...-- ",
                    "4": "....- ",
                    "5": "..... ",
                    "6": "-.... ",
                    "7": "--... ",
                    "8": "---..",
                    "9": "----. ",
                    "0": "----- "
                    }

    string = lst_arg[1].upper()
    for key in string:
        print(NESTED_MORSE[key], end="")
    print("")
    return


if __name__ == "__main__":
    main()
