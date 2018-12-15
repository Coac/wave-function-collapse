import numpy as np


class Cell:
    """
    Cell is a pixel or tile (in 2d) that stores the possible patterns
    """

    def __init__(self, num_pattern):
        self.num_pattern = num_pattern
        self.allowed_patterns = [i for i in range(self.num_pattern)]

    def entropy(self):
        return len(self.allowed_patterns)

    def choose_rnd_pattern(self):
        chosen_index = np.random.randint(len(self.allowed_patterns))
        self.allowed_patterns = [self.allowed_patterns[chosen_index]]

    def is_stable(self):
        return len(self.allowed_patterns) == 1

    def get_value(self):
        if self.is_stable():
            return self.allowed_patterns[0]
        return 4

    def get_neighbors(self):
        return []
        # [(cell, offset)]
