import numpy as np

from pattern import Pattern


class Cell:
    """
    Cell is a pixel or tile (in 2d) that stores the possible patterns
    """

    def __init__(self, num_pattern, position, grid):
        self.num_pattern = num_pattern
        self.allowed_patterns = [i for i in range(self.num_pattern)]

        self.position = position
        self.grid = grid
        self.offsets = [(z, y, x) for x in range(-1, 2) for y in range(-1, 2) for z in range(-1, 2)]

    def entropy(self):
        return len(self.allowed_patterns)

    def choose_rnd_pattern(self):
        chosen_index = np.random.randint(len(self.allowed_patterns))
        self.allowed_patterns = [self.allowed_patterns[chosen_index]]

    def is_stable(self):
        return len(self.allowed_patterns) == 1

    def get_value(self):
        if self.is_stable():
            pattern = Pattern.from_index(self.allowed_patterns[0])
            return pattern.get()
        return -1

    def get_neighbors(self):
        neighbors = []
        for offset in self.offsets:
            neighbor_pos = tuple(np.array(self.position) + np.array(offset))
            out = False
            for i, d in enumerate(neighbor_pos):
                if not 0 <= d < self.grid.size[i]:
                    out = True
            if out:
                continue

            neighbors.append((self.grid.get_cell(neighbor_pos), offset))

        return neighbors
