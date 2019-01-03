"""
An example of using the wave function collapse with 3D voxel file.
It loads a magica voxel file using py-vox-io
You should install py-vox-io using `pip install py-vox-io`
"""

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
    np.random.seed(42)

    grid_size = (6, 6, 6)
    pattern_size = (2, 2, 2)

    sample = load_voxel_sample('../samples/test.vox')

    wfc = WaveFunctionCollapse(grid_size, sample, pattern_size)

    wfc.run()

    image = wfc.get_image()

    export_voxel('../samples/output.vox', image)
