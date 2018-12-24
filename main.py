import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

from wfc import WaveFunctionCollapse

if __name__ == '__main__':

    grid_size = (1, 30, 30)
    pattern_size = (1, 2, 2)

    sample = plt.imread('samples/red_maze.png')

    # Expand dim to 3D
    sample = np.expand_dims(sample, axis=0)
    sample = sample[:, :, :, :3]

    wfc = WaveFunctionCollapse(grid_size, sample, pattern_size)

    # wfc.run()

    fig = plt.figure()

    image = wfc.get_image()
    im = plt.imshow(image)


    def update_fig(*args):
        done = wfc.step()
        if done:
            return im,
        im.set_array(wfc.get_image())
        return im,


    ani = animation.FuncAnimation(fig, update_fig, interval=1, blit=True)
    plt.show()
