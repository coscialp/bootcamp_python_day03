import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


class ImageProcessor:

    @staticmethod
    def load(path):
        img_pil = Image.open(path)
        img = np.array(img_pil)
        print("Loading image of dimension {} x {}".format(img.shape[0], img.shape[1]))
        return img

    @staticmethod
    def display(array):
        plt.imshow(array)
        plt.show()


if __name__ == "__main__":
    imp = ImageProcessor()
    arr = imp.load('./img.png')
    imp.display(arr)

