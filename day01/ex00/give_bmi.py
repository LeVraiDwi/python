import numpy as np


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """fonction qui calcule les imc des par rapport au \
    taille est poids donnee dans height et weiht
    les list doivent avoir les meme dimmension et taille
    les taille ne peuvent etre nul
    calcul: w/(h*h)"""

    if height and not (type(height[0]) is float or type(height[0]) is int):
        print("les list doivent etre des int ou float")
        return []
    if weight and not (type(weight[0]) is float or type(weight[0]) is int):
        print("les list doivent etre des int ou float")
        return []
    if height.count(0) > 0:
        print("les tailles doivent etre strictement superieur a 0")
        return []
    h = np.array(height)
    w = np.array(weight)
    if not w.ndim == h.ndim or not w.size == h.size:
        print("les tableaux ne font pas la meme taille")
        return []
    h = h * h
    ret = w / h
    return ret.tolist()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """retourne un tableau qui pour chaque valeur de bmi un bolean qui indique
    si cette valeur est superieur a 0"""

    if bmi and not (type(bmi[0]) is float or type(bmi[0]) is int):
        print("les list doivent etre des int ou float")
        return []
    return [x > limit for x in bmi]
