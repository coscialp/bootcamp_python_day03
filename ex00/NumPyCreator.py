import numpy as np


class NumPyCreator:

    def from_list(self, lst: list):
        return np.array(lst)

    def from_tuple(self, tpl: tuple):
        return np.array(tpl)

    def from_iterable(self, it):
        return np.array(it)

    def from_shape(self, shape, value: int = 0):
        return np.full(shape, value)

    def random(self, shape):
        return np.random.uniform(0, 1, shape)

    def identity(self, number):
        return np.identity(number)


if __name__ == "__main__":
    npc = NumPyCreator()

    npc.from_list([[1, 2, 3], ['a', 'b', 'c']])
    npc.from_tuple(('a', 'b', 'c'))
    npc.from_iterable(range(0, 5))

    shape = (3, 5)
    npc.from_shape(shape, 5)
    npc.from_shape(shape)





