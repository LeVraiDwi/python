import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    try:
        assert isinstance(start, int), "AssertionError: \
start have the wrong type"
        assert isinstance(end, int), "AssertionError: \
end have the wrong type"
        assert isinstance(family, list), "AssertionError: \
family have the wrong type"
        arr = np.array(family)
        assert arr.ndim == 2, "AssertionError: list is not in two dimension"
    except AssertionError as msg:
        print(msg)
        return []

    print("My shape is : " + str(arr.shape))
    ret = arr[start:end]
    print("My new shape is : " + str(ret.shape))
    return ret.tolist()
