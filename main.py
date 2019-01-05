"""
An example of using the wave function collapse with 2D image.

"""

import matplotlib.pyplot as plt
import numpy as np

from wfc import WaveFunctionCollapse


def plot_patterns(patterns, title=''):
    fig = plt.figure(figsize=(8, 8))
    fig.suptitle(title, fontsize=16)
    columns = 4
    rows = 5
    for i in range(1, columns * rows + 1):
        if i > len(patterns):
            break
        fig.add_subplot(rows, columns, i)
        show(patterns[i - 1])

    plt.show()


def load_sample(path):
    sample = plt.imread(path)
    # Expand dim to 3D
    sample = np.expand_dims(sample, axis=0)
    sample = sample[:, :, :, :3]

    return sample


def show(image):
    if image.shape[0] == 1:
        return plt.imshow(np.squeeze(image, axis=0))


if __name__ == '__main__':

    grid_size = (1, 30, 30)
    pattern_size = (1, 2, 2)

    sample = load_sample('samples/blue.png')
    show(sample)
    plt.show()

    wfc = WaveFunctionCollapse(grid_size, sample, pattern_size)
    plot_patterns(wfc.get_patterns(), 'patterns')

    # _, _, legal_patterns = wfc.propagator.legal_patterns(wfc.patterns[2], (0, 0, 1))
    # show(Pattern.from_index(2).to_image())
    # plt.show()
    # plot_patterns([Pattern.from_index(i).to_image() for i in legal_patterns])

    fig, ax = plt.subplots()
    image = wfc.get_image()
    im = show(image)
    while True:
        done = wfc.step()
        if done:
            break
        image = wfc.get_image()

        if image.shape[0] == 1:
            image = np.squeeze(image, axis=0)
            im.set_array(image)

        fig.canvas.draw()
        plt.pause(0.001)

    plt.show()
