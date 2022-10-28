from .. import Solution, WeightStream
from typing import Iterator
from ..model import Online


class NextFit(Online):

    def _process(self, capacity: int, weights: Iterator[int]) -> Solution:
        bin_index = 0
        solution: Solution = [[]]
        remaining = capacity
        for w in weights:
            if remaining >= w:
                solution[bin_index].append(w)
                remaining = remaining - w
            else:
                bin_index += 1
                solution.append([w])
                remaining = capacity - w
        return solution


class TerribleFit(Online):

    def _process(self, capacity: int, weights: Iterator[int]) -> Solution:
        return [[x] for x in weights]


# NOTE: FirstFit, BestFit, and WorstFit can all be implemented in O(n log n)
# using self balancing binary trees. These implementations does not do this.

class FirstFit(Online):

    def _process(self, capacity: int, weights: Iterator[int]) -> Solution:
        bins: Solution = []
        remaining: list[int] = []

        for weight in weights:
            for i in range(len(remaining)):
                if remaining[i] >= weight:
                    remaining[i] -= weight
                    bins[i].append(weight)
                    break
            else:
                remaining.append(capacity - weight)
                bins.append([weight])

        return bins


class BestFit(Online):

    def _process(self, capacity: int, weights: Iterator[int]) -> Solution:
        bins: Solution = []
        remaining: list[int] = []

        for weight in weights:
            min_diff, best_bin = capacity + 1, -1

            for i, remain in enumerate(remaining):
                diff = remain - weight
                if 0 <= diff < min_diff:
                    min_diff, best_bin = diff, i

            if best_bin == -1:
                remaining.append(capacity - weight)
                bins.append([weight])
            else:
                remaining[best_bin] -= weight
                bins[best_bin].append(weight)

        return bins


class WorstFit(Online):

    def _process(self, capacity: int, weights: Iterator[int]) -> Solution:
        bins: Solution = []
        remaining: list[int] = []

        for weight in weights:
            max_diff, worst_bin = -1, -1

            for i, remain in enumerate(remaining):
                diff = remain - weight
                if diff >= 0 and diff > max_diff:
                    max_diff, worst_bin = diff, i

            if worst_bin == -1:
                remaining.append(capacity - weight)
                bins.append([weight])
            else:
                remaining[worst_bin] -= weight
                bins[worst_bin].append(weight)

        return bins

