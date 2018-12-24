import matplotlib.animation as animation
import matplotlib.pyplot as plt

from wfc import WaveFunctionCollapse

if __name__ == '__main__':

    grid_size = (30, 30)
    pattern_size = (2, 2)

    sample = plt.imread('samples/red_maze.png')
    sample = sample[:, :, :3]

    wfc = WaveFunctionCollapse(grid_size, sample, pattern_size)

    # wfc.run()

    fig = plt.figure()

    im = plt.imshow(wfc.get_image())


    def update_fig(*args):
        done = wfc.step()
        if done:
            return im,
        im.set_array(wfc.get_image())
        return im,


    ani = animation.FuncAnimation(fig, update_fig, interval=1, blit=True)
    plt.show()
