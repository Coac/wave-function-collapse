import matplotlib.pyplot as plt
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
        lowest_entropy_cell = None
        for row in self.board:
            for cell in row:
                entropy = cell.entropy()
                if entropy < min_entropy and not cell.is_stable():
                    min_entropy = min_entropy
                    lowest_entropy_cell = cell

        return lowest_entropy_cell

    def get(self, x, y):
        return self.board[y][x]

    def show(self):
        for x in range(self.size):
            for y in range(self.size):
                print(x, y, self.get(x, y).get_value())
        to_show = []
        for row in self.board:
            to_show.append([cell.get_value() for cell in row])

        cmap = colors.ListedColormap(['white', 'red', 'black', 'blue'])
        im = plt.imshow(to_show, cmap=cmap, interpolation='none', vmin=0, vmax=4)
        plt.colorbar(im)
        plt.show()

    def print_allowed_pattern_count(self):
        to_print = ''
        for x in range(self.size):
            for y in range(self.size):
                to_print += str(len(self.get(x, y).allowed_patterns)) + ' '
            to_print += '\n'
        print(to_print)
