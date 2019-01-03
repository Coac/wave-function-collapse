import os
import time
from multiprocessing import Pool

from pattern import Pattern


class Propagator:
    """
    Propagator that computes and stores the legal patterns relative to another
    """

    def __init__(self, patterns):
        self.patterns = patterns
        self.offsets = [(z, y, x) for x in range(-1, 2) for y in range(-1, 2) for z in range(-1, 2)]

        start_time = time.time()
        self.precompute_legal_patterns()
        print("Patterns constraints generation took %s seconds" % (time.time() - start_time))

    def precompute_legal_patterns(self):
        pool = Pool(os.cpu_count())

        patterns_offsets = []
        for pattern in self.patterns:
            for offset in self.offsets:
                patterns_offsets.append((pattern, offset))

        patterns_compatibility = pool.starmap(self.legal_patterns, patterns_offsets)
        pool.close()
        pool.join()

        for pattern_index, offset, legal_patterns in patterns_compatibility:
            self.patterns[pattern_index].set_legal_patterns(offset, legal_patterns)

    def legal_patterns(self, pattern, offset):
        legal_patt = []
        for candidate_pattern in self.patterns:
            if pattern.is_compatible(candidate_pattern, offset):
                legal_patt.append(candidate_pattern.index)
        pattern.set_legal_patterns(offset, legal_patt)

        return pattern.index, offset, legal_patt

    @staticmethod
    def propagate(cell):
        to_update = [neighbour for neighbour, _ in cell.get_neighbors()]
        while len(to_update) > 0:
            cell = to_update.pop(0)
            for neighbour, offset in cell.get_neighbors():
                for pattern_index in cell.allowed_patterns:
                    pattern = Pattern.from_index(pattern_index)
                    pattern_still_compatible = False
                    for neighbour_pattern_index in neighbour.allowed_patterns:
                        neighbour_pattern = Pattern.from_index(neighbour_pattern_index)

                        if pattern.is_compatible(neighbour_pattern, offset):
                            pattern_still_compatible = True
                            break

                    if not pattern_still_compatible:
                        cell.allowed_patterns.remove(pattern_index)

                        for neigh, _ in cell.get_neighbors():
                            if neigh not in to_update:
                                to_update.append(neigh)
