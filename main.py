import matplotlib.pyplot as plt
import numpy as np

from display import load_sample, show
from wfc import WaveFunctionCollapse

if __name__ == '__main__':

    grid_size = (1, 30, 30)
    pattern_size = (1, 2, 2)

    sample = load_sample('samples/red_maze.png')

    wfc = WaveFunctionCollapse(grid_size, sample, pattern_size)

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
