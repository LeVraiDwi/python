from load_image import ft_load
import numpy as np
from PIL import Image


def zoom(img: Image) -> Image:
    """zoom into the image"""
    crop = img.crop([450, 100, 850, 500])
    img = crop.convert('L')
    return img


def rotate_array(array: np.array) -> np.array:
    """rotate a the array"""
    rotated = np.empty((len(array[0]), len(array)), dtype=np.int16)
    for i in range(len(array)):
        for j in range(len(array[0])):
            rotated[j, i] = array[i, j]
    return rotated


def rotate():
    """diplay rotated image"""
    path = "animal.jpeg"
    array = ft_load(path)
    img = Image.fromarray(array)
    img = zoom(img)
    array = np.asarray(img)
    print("The shape of this image is : " + str(array.shape))
    print(array)
    transposed = rotate_array(array)
    print("New shape after Transpose : " + str(array.shape))
    img = Image.fromarray(transposed)
    print(transposed)
    img.show()
    return


if __name__ == "__main__":
    rotate()
