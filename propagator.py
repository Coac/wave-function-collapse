from display import plot_patterns


class Propagator:
    """
    Propagator that computes and stores the legal patterns relative to another
    """

    def __init__(self, patterns):
        self.patterns = patterns

        self.offsets = [(x, y) for x in range(-1, 2) for y in range(-1, 2)]

        for offset in self.offsets:
            self.legal_patterns(self.patterns[0], offset)

    def legal_patterns(self, pattern, offset):
        legal_patt = []

        shape = pattern.shape

        # area to compare
        start_x = max(offset[0], 0)
        start_y = max(offset[1], 0)

        end_x = min(shape[0] + offset[0], shape[0])
        end_y = min(shape[1] + offset[1], shape[1])

        for candidate_pattern in self.patterns:
            ok_constraint = True

            for x in range(start_x, end_x):
                for y in range(start_y, end_y):
                    if candidate_pattern[y - offset[1], x - offset[0]] != pattern[y, x]:
                        ok_constraint = False
                        break

            if ok_constraint:
                legal_patt.append(candidate_pattern)

        # Add last pattern to plot to check
        legal_patt.append(pattern)
        plot_patterns(legal_patt, offset)

        return self.patterns
