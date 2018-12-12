import numpy as np

from cell import Cell
from pattern import Pattern
from propagator import Propagator

"""
Implementation of WaveFunctionCollapse
Following the "WaveFunctionCollapse is Constraint Solving in the Wild" terminology
"""


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

        self.patterns = Pattern.from_sample(sample)
        self._init_board()
        self.build_propagator()
        for _ in range(100):
            self.observe()
            self.propagate()
        self.output_observations()

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
