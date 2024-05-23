from math import sqrt


def parse_args(func):
    """check if the arg have the right type"""
    def wrapper(*args, **kwargs):
        """Wrapper!! he wrapp like swoop dog"""
        try:
            for arg in args:
                if not isinstance(arg, (int, float)):
                    raise TypeError("ERROR")

            for _, value in kwargs.items():
                if not isinstance(value, str):
                    raise TypeError("ERROR")
        except TypeError as e:
            print(e)
            return None

        return func(*args, **kwargs)

    return wrapper


@parse_args
def ft_statistics(*args: any, **kwargs: any) -> None:
    """affiche les valeur
        traiter selon les commande passer dans kwargs"""

    def mean(numbers: list):
        """return la moyenne de l'ensemble"""
        return (sum(numbers) / len(numbers))

    def median(numbers: list):
        """return la valeur mediane de l'ensemble"""
        numbers.sort()
        size = len(numbers)
        if (size % 2 == 0):
            return (numbers[size] + numbers[size + 1]) / 2
        else:
            return numbers[int(size / 2)]

    def quatileFirst(numbers: list):
        """return le premier quartile de l'ensemble"""
        numbers.sort()
        size = len(numbers)
        if (size % 2 == 0):
            medPos = size / 2 + 1
        else:
            medPos = size / 2
        return numbers[int(medPos / 2)]

    def quatileThird(numbers: list):
        """return le troisieme quartile de l'ensemble"""
        numbers.sort()
        size = len(numbers)
        if (size % 2 == 0):
            medPos = size / 2 + 1
        else:
            medPos = size / 2
        return numbers[int(medPos + (medPos / 2))]

    def ecartType(numbers: list):
        """return l'ecart type de l'ensemble"""
        return sqrt(variance(numbers))

    def variance(numbers: list):
        """return la variance de l'ensemble"""
        m = mean(numbers)
        sum = 0
        for n in numbers:
            sum += (m - n) * (m - n)
        return sum / len(numbers)

    numbers = list(args)
    for _, value in kwargs.items():
        if args is None or len(args) == 0:
            print("ERROR")
            continue
        match value:
            case "mean":
                print(f"mean: {mean(numbers)}")
            case "median":
                print(f"median: {median(numbers)}")
            case "quartile":
                print(f"quartile: [{quatileFirst(numbers)},\
 {quatileThird(numbers)}]")
            case "std":
                print(f"std: {ecartType(numbers)}")
            case "var":
                print(f"var: {variance(numbers)}")
