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
    """cette fonction filtre la liste iter
      en appliquant a chaque element la fonction function
      si function est non definie verifie si l'element est vrai"""
    if (function):
        return Iterator([item for item in iter if function(item)])
    else:
        return Iterator([item for item in iter if item])
