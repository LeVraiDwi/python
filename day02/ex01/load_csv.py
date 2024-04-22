import pandas as pd


def load(path: str) -> pd.DataFrame:
    try:
        assert isinstance(path, str), "assertionError, path should be a string"
        assert path, "assertionError, path is empty"
    except AssertionError as msg:
        print(msg)
        return

    try:
        data = pd.read_csv(path)
    except Exception:
        print("impossible to read the file")
        return

    print("Loading dataset of dimensions %s" % str(data.shape))
    return data
