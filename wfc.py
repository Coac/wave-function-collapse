from grid import Grid
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

    def __init__(self, grid_size, sample):
        self.patterns = Pattern.from_sample(sample)
        self.grid = self._create_grid(grid_size)

        self.propagator = None

    def run(self):
        self.build_propagator()
        while True:
            self.grid.print_allowed_pattern_count()
            cell = self.observe()
            if cell is None:
                break
            self.propagate(cell)
        self.output_observations()

    def build_propagator(self):
        self.propagator = Propagator(self.patterns)

    def observe(self):
        if self.grid.check_contradiction():
            return None
        cell = self.grid.find_lowest_entropy()

        if cell is None:
            return None

        cell.choose_rnd_pattern()

        return cell

    def propagate(self, cell):
        self.propagator.propagate(cell)

    def output_observations(self):
        self.grid.show()

    def _create_grid(self, grid_size):
        num_pattern = len(self.patterns)
        return Grid(grid_size, num_pattern)
