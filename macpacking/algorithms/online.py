from .. import Solution, WeightStream
from typing import Iterator
from ..model import Online


class NextFit(Online):

    def _process(self, capacity: int, weights: Iterator[int]) -> Solution:
        bin_index = 0
        solution = [[]]
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
