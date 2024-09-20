class Iterator:
    def __init__(self, iterable):
        self.limit = len(iterable)
        self.iter = iterable
        self.index = 0

    def __next__(self):
        if self.index < self.limit:
            result = self.iter[self.index]
            self.index = self.index + 1
            return result
        else:
            raise StopIteration

    def __getitem__(self, index):
        return self.iter[index]

    def __iter___(self):
        return iter(self)


def ft_filter(function, iter) -> Iterator:
    """Return an iterator yielding those items of iterable for which \
function(item)
is true. If function is None, return the items that are true."""
    if (function):
        return Iterator([item for item in iter if function(item)])
    else:
        return Iterator([item for item in iter if item])
