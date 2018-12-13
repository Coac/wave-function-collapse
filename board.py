from cell import Cell


class Board:
    """
    Board is made of Cells
    """

    def __init__(self, size, num_pattern):
        self.size = size
        self.board = [[Cell(num_pattern) for _ in range(self.size)] for _ in range(self.size)]

    def find_lowest_entropy(self):
        min_entropy = 999999
        lowest_entropy_cell = None
        for row in self.board:
            for cell in row:
                entropy = cell.entropy()
                if entropy < min_entropy:
                    min_entropy = min_entropy
                    lowest_entropy_cell = cell

        return lowest_entropy_cell
