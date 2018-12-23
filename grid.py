import matplotlib.pyplot as plt
import numpy as np

from cell import Cell
from pattern import Pattern


class Grid:
    """
    Grid is made of Cells
    """

    def __init__(self, size, num_pattern):
        self.size = size
        self.grid = np.empty(self.size, dtype=object)
        for position in np.ndindex(self.size):
            self.grid[position] = Cell(num_pattern, position[::-1], self)

        # self.grid = np.array([[Cell(num_pattern, (x, y), self) for x in range(self.size)] for y in range(self.size)])
        # self.grid = np.array([Cell(num_pattern, (x,), self) for x in range(self.size)])

    def find_lowest_entropy(self):
        min_entropy = 999999
        lowest_entropy_cells = []
        for cell in self.grid.flat:
            if cell.is_stable():
                continue

            entropy = cell.entropy()

            if entropy == min_entropy:
                lowest_entropy_cells.append(cell)
            elif entropy < min_entropy:
                min_entropy = entropy
                lowest_entropy_cells = [cell]

        if len(lowest_entropy_cells) == 0:
            return None
        cell = lowest_entropy_cells[np.random.randint(len(lowest_entropy_cells))]
        return cell

    def get_cell(self, index):
        """
        :param index: (x, y, z...)
        :return: cell
        """
        reversed_index = index[::-1]
        return self.grid[reversed_index]

    def get_image(self):
        image = np.vectorize(lambda c: c.get_value())(self.grid)
        image = Pattern.index_to_img(image)
        return image

    def show(self):
        plt.imshow(self.get_image())
        plt.show()

    def check_contradiction(self):
        for cell in self.grid.flat:
            if len(cell.allowed_patterns) == 0:
                return True
        return False

    def print_allowed_pattern_count(self):
        grid_allowed_patterns = np.vectorize(lambda c: len(c.allowed_patterns))(self.grid)
        print(grid_allowed_patterns)
