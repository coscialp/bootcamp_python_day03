import numpy as np
import matplotlib.pyplot as plt
import PIL.Image as pimg
from ImageProcessor import ImageProcessor as Ip


class ColorFilter:

    @staticmethod
    def invert(array):
        return 255 - array

    @staticmethod
    def to_blue(array):
        array[:, :, 0:2] = 0
        return array

    @staticmethod
    def to_red(array):
        array[:, :, 1:] = 0
        return array

    @staticmethod
    def to_yellow(array):
        array[:, :, 2:] = 0
        return array

    @staticmethod
    def to_green(array):
        array[:, :, (0, 2)] = 0
        return array


if __name__ == '__main__':
    arr = Ip.load('chat.jpg')

    print(arr)
    new_arr = ColorFilter.to_yellow(arr)
    print(new_arr)
    Ip.display(new_arr)
