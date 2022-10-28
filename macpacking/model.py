from abc import ABC, abstractmethod
from typing import Iterator
from . import WeightStream, WeightSet, Solution


class BinPacker(ABC):
    pass


class Online(BinPacker):

    def __call__(self, ws: WeightStream):
        return self._process(*ws)

    @abstractmethod
    def _process(self, capacity: int, weights: Iterator[int]) -> Solution:
        pass


class Offline(BinPacker):

    def __call__(self, ws: WeightSet):
        return self._process(*ws)

    @abstractmethod
    def _process(self, capacity: int, weights: list[int]) -> Solution:
        pass
