import numpy as np

from display import plot_sample, plot_patterns


class Pattern:
    """
    Pattern is a configuration of tiles from the input image.
    """

    def __init__(self, data):
        self.index = 0
        self.data = np.array(data)
        pass

    def get(self, x, y):
        return self.data[y, x]

    @property
    def shape(self):
        return self.data.shape

    def is_compatible(self, candidate_pattern, offset):
        assert (self.shape == candidate_pattern.shape)

        start_x = max(offset[0], 0)
        start_y = max(offset[1], 0)

        end_x = min(self.shape[0] + offset[0], self.shape[0])
        end_y = min(self.shape[1] + offset[1], self.shape[1])

        ok_constraint = True
        for x in range(start_x, end_x):
            for y in range(start_y, end_y):
                if candidate_pattern.get(x - offset[0], y - offset[1]) != self.get(x, y):
                    ok_constraint = False
                    break

        return ok_constraint

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
                patterns.append(Pattern(pattern))

                # TODO Rotate

                # TODO Reflect

        plot_patterns(patterns)
        return patterns
