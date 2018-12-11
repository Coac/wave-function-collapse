import numpy as np

from display import plot_patterns, plot_sample

"""
Implementation of WaveFunctionCollapse
Following the "WaveFunctionCollapse is Constraint Solving in the Wild" terminology
"""


def inverse_offset(offset):
    return -offset[0], -offset[1]


class Propagator:
    """
    Propagator that computes and stores the legal patterns relative to another
    """

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


class Pattern:
    """
    Pattern is a configuration of tiles from the input image.
    """

    def __init__(self):
        self.index = 0
        pass


class Cell:
    """
    Cell is a pixel or tile (in 2d) that stores the possible patterns
    """

    def __init__(self, num_pattern):
        self.num_pattern = num_pattern
        self.allowed_pattern = {}
        for i in range(num_pattern):
            self.allowed_pattern[i] = True

    def entropy(self):
        allowed_count = 0
        for i in range(self.num_pattern):
            allowed_count += self.allowed_pattern[i]
        return allowed_count


class WaveFunctionCollapse:
    """
    WaveFunctionCollapse encapsulates the wfc algorithm
    """

    def __init__(self):
        self.patterns = []
        self.propagator = None
        self.N = 10

    def run(self):
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

        self.patterns_from_sample(sample, shape)
        self._init_board()
        self.build_propagator()
        for _ in range(100):
            self.observe()
            self.propagate()
        self.output_observations()

    def patterns_from_sample(self, sample, shape):
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
        self.propagator = Propagator(self.patterns)

    def observe(self):
        return self._find_lowest_entropy()

    def propagate(self):
        pass

    def output_observations(self):
        pass

    def _find_lowest_entropy(self):
        return self.board[0]

    def _init_board(self):
        num_pattern = len(self.patterns)

        self.board = [[None for _ in range(self.N)] for _ in range(self.N)]
        for i in range(self.N):
            for j in range(self.N):
                self.board[i][j] = Cell(num_pattern)


if __name__ == '__main__':
    wfc = WaveFunctionCollapse()
    wfc.run()
