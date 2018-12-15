import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors

from cell import Cell


class Board:
    """
    Board is made of Cells
    """

    def __init__(self, size, num_pattern):
        self.size = size
        self.board = [[Cell(num_pattern, (x, y), self) for x in range(self.size)] for y in range(self.size)]

    def find_lowest_entropy(self):
        min_entropy = 999999
        lowest_entropy_cells = []
        for row in self.board:
            for cell in row:
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

    def get(self, x, y):
        return self.board[y][x]

    def show(self):
        to_show = []
        for row in self.board:
            to_show.append([cell.get_value() for cell in row])

        cmap = colors.ListedColormap(['white', 'red', 'black', 'blue'])
        im = plt.imshow(to_show, cmap=cmap, interpolation='none', vmin=0, vmax=4)
        plt.colorbar(im)
        plt.show()

    def check_contradiction(self):
        for row in self.board:
            for cell in row:
                if len(cell.allowed_patterns) == 0:
                    return True
        return False

    def print_allowed_pattern_count(self):
        to_print = ''
        for y in range(self.size):
            for x in range(self.size):
                to_print += str(len(self.get(x, y).allowed_patterns)) + '\t'
            to_print += '\n'
        print(to_print)
