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

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """return le produit des vecteur v1 et v2"""
        calculator.check_vector(V1, V2)
        ret: float = 0
        for i in range(len(V1)):
            ret += V1[i] * V2[i]
        print(f"Dot product is: {ret}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """return l'addition des vecteur v1 et v2"""
        calculator.check_vector(V1, V2)
        ret: list[float] = []
        for i in range(len(V1)):
            ret.append(V1[i] + V2[i])
        print(f"Add Vector is: {ret}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """return la soustraction des vecteur v1 et v2"""
        calculator.check_vector(V1, V2)
        ret: list[float] = []
        for i in range(len(V1)):
            ret.append(V1[i] - V2[i])
        print(f"Sous Vector is: {ret}")

    @staticmethod
    def check_vector(V1: list, V2: list):
        """verifie si les vecteur sont bien des\
 liste de nombre qui font la meme taille"""
        if not isinstance(V1, list):
            raise AssertionError("vector should be a list")
        for num in V1:
            if not isinstance(num, int) and not isinstance(num, float):
                raise AssertionError("vector should be fill with number")
        if not isinstance(V2, list):
            raise AssertionError("vector should be a list")
        for num in V2:
            if not isinstance(num, int) and not isinstance(num, float):
                raise AssertionError("vector should be fill with number")
        if len(V1) != len(V2):
            raise AssertionError("vector should have the same size")
