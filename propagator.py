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
        for candidate_pattern in self.patterns:
            if pattern.is_compatible(candidate_pattern, offset):
                legal_patt.append(candidate_pattern)

        # Add last pattern to plot to check
        legal_patt.append(pattern)
        plot_patterns(legal_patt, offset)

        return self.patterns
