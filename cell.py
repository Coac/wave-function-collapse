import numpy as np


class Cell:
    """
    Cell is a pixel or tile (in 2d) that stores the possible patterns
    """

    def __init__(self, num_pattern):
        self.num_pattern = num_pattern
        self.allowed_pattern = {}
        for i in range(self.num_pattern):
            self.allowed_pattern[i] = True

    def entropy(self):
        allowed_count = 0
        for i in range(self.num_pattern):
            allowed_count += self.allowed_pattern[i]
        return allowed_count

    def choose_rnd_pattern(self):
        allowed_indexes = []
        for i, is_allowed in enumerate(self.allowed_pattern):
            if not is_allowed:
                continue
            allowed_indexes.append(i)

        chosen_index = np.random.randint(len(allowed_indexes))

        for i in range(self.num_pattern):
            if i == chosen_index:
                continue
            self.allowed_pattern[i] = False
