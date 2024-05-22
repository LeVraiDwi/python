class calculator():
    """classe qui contient un vecteur sur \
lequel on peut effectuer es operation"""
    def __init__(self, vector: list) -> None:
        """initialise la classe"""
        if not isinstance(vector, list):
            raise AssertionError("vector should be a list")
        for num in vector:
            if not isinstance(num, int) and not isinstance(num, float):
                raise AssertionError("vector should be fill with number")
        self.vector = vector

    def __add__(self, object) -> None:
        """additionne a chaque valeur du vecteur object"""
        for i in range(len(self.vector)):
            self.vector[i] += object
        print(self.vector)

    def __mul__(self, object) -> None:
        """multiplie chaque valeur du vecteur object"""
        for i in range(len(self.vector)):
            self.vector[i] *= object
        print(self.vector)

    def __sub__(self, object) -> None:
        """soustrait a chaque valeur du vecteur object"""
        for i in range(len(self.vector)):
            self.vector[i] -= object
        print(self.vector)

    def __truediv__(self, object) -> None:
        """divise chaque valeur du vecteur object"""
        if object == 0:
            raise AssertionError("can't make a dicision by 0")
        for i in range(len(self.vector)):
            self.vector[i] /= object
        print(self.vector)
