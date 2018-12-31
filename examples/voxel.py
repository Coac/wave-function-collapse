import numpy as np
from pyvox.models import Vox
from pyvox.parser import VoxParser
from pyvox.writer import VoxWriter

from wfc import WaveFunctionCollapse


def load_voxel_sample(path):
    vox_parser = VoxParser(path).parse()
    sample = vox_parser.to_dense()
    sample = np.expand_dims(sample, axis=3)
    return sample


def export_voxel(path, image):
    print("image shape:", image.shape)
    image = wfc.get_image()
    image = np.squeeze(image, axis=3)
    image = image.astype(int)
    vox = Vox.from_dense(image)
    VoxWriter(path, vox).write()


if __name__ == '__main__':
    grid_size = (10, 10, 10)
    pattern_size = (2, 2, 2)

    sample = load_voxel_sample('../samples/test.vox')

    wfc = WaveFunctionCollapse(grid_size, sample, pattern_size)

    wfc.run()

    image = wfc.get_image()

    export_voxel('../samples/output.vox', image)
