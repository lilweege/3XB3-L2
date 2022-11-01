from abc import ABC, abstractmethod
from typing import Iterator
from dataclasses import dataclass, field
from math import ceil
from . import WeightStream, WeightSet, Solution


@dataclass(order=True)
class BinPackerResult:
    capacity: int = field(compare=False, repr=False)
    solution: Solution = field(compare=False, repr=False)
    num_bins: int = field(init=False)
    wastefulness: float = field(init=False)

    def __post_init__(self):
        self.num_bins = len(self.solution)
        half_cap = ceil(self.capacity / 2)
        max_fullness = half_cap * self.num_bins
        measure = (abs(half_cap - sum(weights)) for weights in self.solution)
        self.wastefulness = max_fullness - round(sum(measure) / self.num_bins, 4)


class BinPacker(ABC):
    pass


class Online(BinPacker):

    def __call__(self, ws: WeightStream) -> BinPackerResult:
        capacity, weights = ws
        return BinPackerResult(capacity, self._process(capacity, weights))

    @abstractmethod
    def _process(self, capacity: int, weights: Iterator[int]) -> Solution:
        pass


class Offline(BinPacker):

    def __call__(self, ws: WeightSet) -> BinPackerResult:
        capacity, weights = ws
        return BinPackerResult(capacity, self._process(capacity, weights))

    @abstractmethod
    def _process(self, capacity: int, weights: list[int]) -> Solution:
        pass
