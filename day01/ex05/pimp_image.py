import numpy as np
from PIL import Image


def ft_invert(array: np.array) -> np.array:
    """Inverts the color of the image received."""
    inverted = np.copy(array)
    for i in range(len(inverted)):
        for j in range(len(inverted[0])):
            for k in range(len(inverted[0][0])):
                inverted[i, j, k] = 255 - inverted[i, j, k]
    img = Image.fromarray(inverted)
    img.show()
    return


def ft_red(array: np.array) -> np.array:
    """apply a red philter on the image received."""
    inverted = np.copy(array)
    for i in range(len(inverted)):
        for j in range(len(inverted[0])):
            inverted[i, j, 0] = inverted[i, j, 0]
            inverted[i, j, 1] = 0 * inverted[i, j, 1]
            inverted[i, j, 2] = 0 * inverted[i, j, 2]
    img = Image.fromarray(inverted)
    img.show()
    return


def ft_green(array: np.array) -> np.array:
    """apply a green philter on the image received."""
    inverted = np.copy(array)
    for i in range(len(inverted)):
        for j in range(len(inverted[0])):
            inverted[i, j, 1] = inverted[i, j, 1]
            inverted[i, j, 0] = inverted[i, j, 0] - inverted[i, j, 0]
            inverted[i, j, 2] = inverted[i, j, 2] - inverted[i, j, 2]
    img = Image.fromarray(inverted)
    img.show()
    return


def ft_blue(array: np.array) -> np.array:
    """apply a blue philter on the image received."""
    inverted = np.copy(array)
    for i in range(len(inverted)):
        for j in range(len(inverted[0])):
            inverted[i, j, 2] = inverted[i, j, 2]
            inverted[i, j, 1] = 0
            inverted[i, j, 0] = 0
    img = Image.fromarray(inverted)
    img.show()
    return


def ft_grey(array: np.array) -> np.array:
    """turn the image received in a grey scale."""
    inverted = np.empty((array.shape[0], array.shape[1]), dtype=np.int16)
    print(inverted.shape)
    for i in range(len(inverted)):
        for j in range(len(inverted[0])):
            a = np.array(array[i, j])
            inverted[i, j] = a.sum() / 3
    img = Image.fromarray(inverted)
    print(inverted)
    img.show()
    return
