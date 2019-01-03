"""
An example of using the wave function collapse with 2D image.

"""

import matplotlib.pyplot as plt
import numpy as np

from display import load_sample, show
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


if __name__ == '__main__':

    grid_size = (1, 30, 30)
    pattern_size = (1, 2, 2)

    sample = load_sample('samples/red_maze.png')

    wfc = WaveFunctionCollapse(grid_size, sample, pattern_size)
    plot_patterns(wfc.get_patterns(), 'patterns')

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
