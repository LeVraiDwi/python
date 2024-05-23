def square(x: int | float) -> int | float:
    """return the square of x"""
    try:
        assert isinstance(x, (int, float)), "x should be number"
    except AssertionError as msg:
        print(msg)
    return x * x


def pow(x: int | float) -> int | float:
    """return the expnentiation of x by himself"""
    try:
        assert isinstance(x, (int, float)), "x should be number"
    except AssertionError as msg:
        print(msg)

    return x ** x


def outer(x: int | float, function) -> object:
    """returns an object that when called
    returns the result of the arguments calculation"""
    count = 0
    value = x

    def inner() -> float:
        nonlocal count
        nonlocal value
        value = function(value)
        count += 1
        return value
    return inner
