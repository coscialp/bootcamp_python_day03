import numpy as np


class ScrapBooker:

    @staticmethod
    def crop(array, dimension, position=(0, 0)):
        if dimension[0] > array.shape[0] or dimension[1] > array.shape[1]:
            print("ERROR")
            return
        y, x = array.shape
        start_x = position[1]
        start_y = position[0]
        return array[start_y:start_y+dimension[0], start_x:start_x+dimension[1]]

    @staticmethod
    def thin(array, n, axis):
        if axis == 0:
            return np.delete(array, slice(0, len(array), n), axis)
        elif axis == 1:
            return np.delete(array, slice(0, len(array[0]), n), axis)

    @staticmethod
    def juxtapose(array, n, axis):
        lst = []
        for i in range(0, n):
            lst.append(array)
        return np.concatenate(lst, axis)

    @staticmethod
    def mosaic(array, dimensions):
        return np.tile(array, (dimensions[0], dimensions[1] - array.shape[1]))


if __name__ == "__main__":
    arr = np.random.randint(0, 100, (1, 2))
    print(arr)
    arr = ScrapBooker.mosaic(arr, (4, 4))
    print()
    print(arr)



