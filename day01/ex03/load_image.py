from PIL import Image
import numpy as np


def ft_load(path: str) -> np.array:
    """Function that return a array rgb format from a image
    set in path"""
    try:
        assert isinstance(path, str), \
            "path should be a string"
    except AssertionError as msg:
        print(msg)
        return
    try:
        image = Image.open(path)
    except Exception:
        print("can' t open the image")
        return []
    dataArray = np.asarray(image)
    return dataArray
