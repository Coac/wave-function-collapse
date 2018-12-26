import os

import matplotlib.pyplot as plt
import numpy as np
from pyvox.parser import VoxParser


def load_sample(path):
    _, file_extension = os.path.splitext(path)

    if file_extension == '.vox':
        m = VoxParser(path).parse()
        sample = m.to_dense()
        sample = np.expand_dims(sample, axis=3)
        return sample

    sample = plt.imread(path)
    # Expand dim to 3D
    sample = np.expand_dims(sample, axis=0)
    sample = sample[:, :, :, :3]

    return sample


def show(image):
    if image.shape[0] == 1:
        return plt.imshow(np.squeeze(image, axis=0))
