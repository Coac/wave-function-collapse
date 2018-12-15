import numpy as np

from board import Board
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
        self.board = None

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
            cell = self.observe()
            self.propagate(cell)
        self.output_observations()

    def build_propagator(self):
        self.propagator = Propagator(self.patterns)

    def observe(self):
        cell = self.board.find_lowest_entropy()

        # TODO check for contradiction
        # TODO check for end

        cell.choose_rnd_pattern()

        return cell

    def propagate(self, cell):
        self.propagator.propagate(cell)

    def output_observations(self):
        self.board.show()

    def _init_board(self):
        num_pattern = len(self.patterns)
        self.board = Board(10, num_pattern)


if __name__ == '__main__':
    wfc = WaveFunctionCollapse()
    wfc.run()
