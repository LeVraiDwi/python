def callLimit(limit: int):
    """decrator taht limits the number
    of time you can call the function"""
    count = 0

    def callLimiter(function):
        """Wrapper!! he wrapp like swoop dog"""

        def limit_function(*args: any, **kwds: any):
            """check if the count is under the limit
            and increment it"""
            nonlocal count
            if count < limit:
                count += 1
                return function(*args, **kwds)
            else:
                print(f"Error: <{function.__name__} at \
{hex(id(function))}> call too many times")
        return limit_function
    return callLimiter
