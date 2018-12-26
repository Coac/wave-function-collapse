import matplotlib.pyplot as plt
import numpy as np


def load_sample(path):
    sample = plt.imread(path)

    # Expand dim to 3D
    sample = np.expand_dims(sample, axis=0)
    sample = sample[:, :, :, :3]

    return sample


def show(image):
    if image.shape[0] == 1:
        plt.imshow(np.squeeze(image, axis=0))
    else:
        # TODO 3D
        plt.imshow(image)
