from load_image import ft_load
import numpy as np
from PIL import Image


def zoom(img: Image) -> Image:
    crop = img.crop([450, 100, 850, 500])
    img = crop.convert('L')
    return img


def main():
    path = "animal.jpeg"

    array = ft_load(path)
    img = Image.fromarray(array)
    print("The shape of this image is : " + str(array.shape))
    print(array)
    img = zoom(img)
    array = np.asarray(img)
    print("New shape after slicing : " + str(array.shape))
    print(array)
    img.show()


if __name__ == "__main__":
    main()
