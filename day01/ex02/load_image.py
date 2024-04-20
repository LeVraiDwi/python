from PIL import Image
from numpy import asarray


def ft_load(path: str):
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
    dataArray = asarray(image)
    print("The shape of this image is : " + str(dataArray.shape))
    return dataArray
