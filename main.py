import numpy as np

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

    wfc.run()
