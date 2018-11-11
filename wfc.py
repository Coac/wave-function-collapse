import numpy as np

from display import plot_patterns, plot_sample


class Propagator:
    def __init__(self, patterns):
        self.patterns = patterns

        self.offsets = [(x, y) for x in range(-1, 2) for y in range(-1, 2)]

        for offset in self.offsets:
            self.legal_patterns(self.patterns[0], offset)

    def legal_patterns(self, pattern, offset):
        legal = []

        shape = pattern.shape

        # area to compare
        start_x = 0 + (offset[0] if offset[0] > 0 else 0)
        start_y = 0 + (offset[1] if offset[1] > 0 else 0)

        end_x = shape[0] + (offset[0] if offset[0] < 0 else 0)
        end_y = shape[1] + (offset[1] if offset[1] < 0 else 0)

        for candidate_pattern in self.patterns:
            ok_constraint = True
            for x in range(start_x, end_x):
                for y in range(start_y, end_y):
                    if candidate_pattern[x + offset[0] * -1, y + offset[1] * -1] != pattern[x, y]:
                        ok_constraint = False
                        break

            if ok_constraint:
                legal.append(candidate_pattern)

        legal.append(pattern)

        plot_patterns(legal, offset)

        return self.patterns


class WaveFunctionCollapse:
    def __init__(self):
        self.patterns = []

    def run(self):
        self.patterns_from_sample()
        self.build_propagator()
        for _ in range(100):
            self.observe()
            self.propagate()
        self.output_observations()

    def patterns_from_sample(self):
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

        plot_sample(sample)

        self.patterns = []
        pattern_size = (2, 2)
        for x in range(0, shape[0] - pattern_size[0] + 1):
            for y in range(0, shape[1] - pattern_size[1] + 1):
                x_range = range(x, pattern_size[0] + x)
                y_range = range(y, pattern_size[1] + y)

                pattern = sample[np.ix_(x_range, y_range)]
                self.patterns.append(pattern)

                # TODO Rotate

                # TODO Reflect

        plot_patterns(self.patterns)

    def build_propagator(self):
        Propagator(self.patterns)
        pass

    def observe(self):
        pass

    def propagate(self):
        pass

    def output_observations(self):
        pass


if __name__ == '__main__':
    wfc = WaveFunctionCollapse()
    wfc.run()
