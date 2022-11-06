from abc import ABC, abstractmethod
from typing import Iterator
from dataclasses import dataclass, field
from math import ceil
from . import WeightStream, WeightSet, Solution


@dataclass(order=True)
class BinPackerResult:
    solution: Solution = field(compare=False, repr=False)


@dataclass(order=True)
class ConstantCapacityResult(BinPackerResult):
    capacity: int = field(compare=False, repr=False)
    num_bins: int = field(init=False)
    wastefulness: float = field(init=False)

    def __post_init__(self):
        self.num_bins = len(self.solution)
        half_cap = ceil(self.capacity / 2)
        max_fullness = half_cap * self.num_bins
        measure = (abs(half_cap - sum(weights)) for weights in self.solution)
        self.wastefulness = max_fullness - sum(measure)


@dataclass(order=True)
class ConstantBinsResult(BinPackerResult):
    num_bins: int = field(compare=False, repr=False)
    largest: int = field(init=False)
    difference: int = field(init=False)

    def __post_init__(self):
        self.largest = max(sum(weights) for weights in self.solution)
        smallest = min(sum(weights) for weights in self.solution)
        self.difference = self.largest - smallest


class BinPacker(ABC):
    pass


class Online(BinPacker):

    @abstractmethod
    def _process(self, upper_bound: int, weights: Iterator[int]) -> Solution:
        pass


class Offline(BinPacker):

    @abstractmethod
    def _process(self, upper_bound: int, weights: list[int]) -> Solution:
        pass


class OnlineConstantCapacity(Online):

    def __call__(self, ws: WeightStream) -> BinPackerResult:
        capacity, weights = ws
        return ConstantCapacityResult(self._process(capacity, weights), capacity)


class OnlineConstantBins(Online):

    def __call__(self, ws: WeightStream) -> BinPackerResult:
        num_bins, weights = ws
        return ConstantBinsResult(self._process(num_bins, weights), num_bins)


class OfflineConstantCapacity(Offline):

    def __call__(self, ws: WeightSet) -> BinPackerResult:
        capacity, weights = ws
        return ConstantCapacityResult(self._process(capacity, weights), capacity)


class OfflineConstantBins(Offline):

    def __call__(self, ws: WeightSet) -> BinPackerResult:
        num_bins, weights = ws
        return ConstantBinsResult(self._process(num_bins, weights), num_bins)


