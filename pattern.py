import numpy as np

from display import plot_sample, plot_patterns


class Pattern:
    """
    Pattern is a configuration of tiles from the input image.
    """

    def __init__(self):
        self.index = 0
        pass

    @staticmethod
    def from_sample(sample):
        plot_sample(sample)

        shape = sample.shape
        patterns = []
        pattern_size = (2, 2)
        for x in range(0, shape[0] - pattern_size[0] + 1):
            for y in range(0, shape[1] - pattern_size[1] + 1):
                x_range = range(x, pattern_size[0] + x)
                y_range = range(y, pattern_size[1] + y)

                pattern = sample[np.ix_(x_range, y_range)]
                patterns.append(pattern)

                # TODO Rotate

                # TODO Reflect

        plot_patterns(patterns)
        return patterns
