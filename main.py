import matplotlib.pyplot as plt
import numpy as np
from pyvox.models import Vox
from pyvox.writer import VoxWriter

from display import load_sample, show
from wfc import WaveFunctionCollapse

if __name__ == '__main__':

    grid_size = (10, 10, 10)
    pattern_size = (2, 2, 2)

    # sample = load_sample('samples/red_maze.png')
    sample = load_sample('samples/test.vox')

    wfc = WaveFunctionCollapse(grid_size, sample, pattern_size)

    # wfc.run()

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

    print("image shape:", image.shape)
    if len(image.shape) == 4:
        print("-----------------")
        image = wfc.get_image()
        image = np.squeeze(image, axis=3)
        image = image.astype(int)
        print(image)
        print(image.shape)
        vox = Vox.from_dense(image)
        VoxWriter('output.vox', vox).write()

    plt.show()
