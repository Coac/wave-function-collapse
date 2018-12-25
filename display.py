import matplotlib.pyplot as plt
import numpy as np


def show(image):
    if image.shape[0] == 1:
        plt.imshow(np.squeeze(image, axis=0))
    else:
        # TODO 3D
        plt.imshow(image)
