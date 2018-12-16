import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors

from wfc import WaveFunctionCollapse

if __name__ == '__main__':
    grid_size = 10

    shape = (4, 4)
    sample = np.zeros(shape)
    sample[2, 2] = 1
    sample[1, 1] = 2
    sample[2, 1] = 2
    sample[3, 1] = 2
    sample[1, 2] = 2
    sample[1, 3] = 2
    sample[2, 3] = 2
    sample[3, 3] = 2
    sample[3, 2] = 2

    wfc = WaveFunctionCollapse(grid_size, sample)

    # wfc.run()

    fig = plt.figure()
    cmap = colors.ListedColormap(['white', 'red', 'black', 'blue'])
    im = plt.imshow(wfc.get_image(), cmap=cmap, animated=True, interpolation='none', vmin=0, vmax=4)
    plt.colorbar(im)


    def update_fig(*args):
        done = wfc.step()
        if done:
            return im,
        im.set_array(wfc.get_image())
        return im,


    ani = animation.FuncAnimation(fig, update_fig, interval=1, blit=True)
    plt.show()
