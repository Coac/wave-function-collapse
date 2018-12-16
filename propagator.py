from pattern import Pattern


class Propagator:
    """
    Propagator that computes and stores the legal patterns relative to another
    """

    def __init__(self, patterns):
        self.patterns = patterns

        self.offsets = [(x, y) for x in range(-1, 2) for y in range(-1, 2)]

        for pattern in self.patterns:
            for offset in self.offsets:
                self.legal_patterns(pattern, offset)

        # TODO store a precomputed compatibility list

    def legal_patterns(self, pattern, offset):
        legal_patt = []
        for candidate_pattern in self.patterns:
            if pattern.is_compatible(candidate_pattern, offset):
                legal_patt.append(candidate_pattern.index)

        # plot_patterns([Pattern.index_to_pattern[pat] for pat in legal_patt], offset)

        return legal_patt

    def propagate(self, cell):
        to_update = [neighbour for neighbour, _ in cell.get_neighbors()]
        while len(to_update) > 0:
            cell = to_update.pop(0)
            for neighbour, offset in cell.get_neighbors():
                for pattern_index in cell.allowed_patterns:
                    pattern = Pattern.index_to_pattern[pattern_index]
                    pattern_still_compatible = False
                    for neighbour_pattern_index in neighbour.allowed_patterns:
                        neighbour_pattern = Pattern.index_to_pattern[neighbour_pattern_index]

                        if pattern.is_compatible(neighbour_pattern, offset):
                            pattern_still_compatible = True
                            break

                    if not pattern_still_compatible:
                        cell.allowed_patterns.remove(pattern_index)

                        for neigh, _ in cell.get_neighbors():
                            if neigh not in to_update:
                                to_update.append(neigh)
