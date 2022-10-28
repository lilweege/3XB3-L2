from .. import Solution, WeightSet
from ..model import Offline
from .online import NextFit as Nf_online
from .online import FirstFit as Ff_online
from .online import BestFit as Bf_online
from .online import WorstFit as Wf_online


class NextFit(Offline):

    def _process(self, capacity: int, weights: list[int]) -> Solution:
        '''An offline version of NextFit, ordering the weigh stream and
        delegating to the online version (avoiding code duplication)'''
        weights = sorted(weights, reverse=True)
        delegation = Nf_online()
        return delegation((capacity, iter(weights)))


class FirstFitDecreasing(Offline):

    def _process(self, capacity: int, weights: list[int]) -> Solution:
        weights = sorted(weights, reverse=True)
        delegation = Ff_online()
        return delegation((capacity, iter(weights)))


class BestFitDecreasing(Offline):

    def _process(self, capacity: int, weights: list[int]) -> Solution:
        weights = sorted(weights, reverse=True)
        delegation = Bf_online()
        return delegation((capacity, iter(weights)))


class WorstFitDecreasing(Offline):

    def _process(self, capacity: int, weights: list[int]) -> Solution:
        weights = sorted(weights, reverse=True)
        delegation = Wf_online()
        return delegation((capacity, iter(weights)))
