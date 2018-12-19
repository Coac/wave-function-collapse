import matplotlib.animation as animation
import matplotlib.pyplot as plt
from matplotlib import colors

from wfc import WaveFunctionCollapse

if __name__ == '__main__':

    grid_size = 30
    sample = plt.imread('samples/red_maze.png')
    wfc = WaveFunctionCollapse(grid_size, sample)

    # wfc.run()

    fig = plt.figure()
    cmap = colors.ListedColormap(['white', 'red', 'black', 'grey'])
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
