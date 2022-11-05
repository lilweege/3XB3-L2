from .. import Solution, WeightSet
from ..model import Offline
from .online import NextFit as Nf_online, FirstFit, BestFit, WorstFit, RefinedFirstFit


class NextFit(Offline):

    def _process(self, capacity: int, weights: list[int]) -> Solution:
        '''An offline version of NextFit, ordering the weigh stream and
        delegating to the online version (avoiding code duplication)'''
        weights = sorted(weights, reverse=True)
        delegation = Nf_online()
        return delegation((capacity, iter(weights))).solution


class FirstFitDecreasing(Offline):

    def _process(self, capacity: int, weights: list[int]) -> Solution:
        weights = sorted(weights, reverse=True)
        delegation = FirstFit()
        return delegation((capacity, iter(weights))).solution


class BestFitDecreasing(Offline):

    def _process(self, capacity: int, weights: list[int]) -> Solution:
        weights = sorted(weights, reverse=True)
        delegation = BestFit()
        return delegation((capacity, iter(weights))).solution


class WorstFitDecreasing(Offline):

    def _process(self, capacity: int, weights: list[int]) -> Solution:
        weights = sorted(weights, reverse=True)
        delegation = WorstFit()
        return delegation((capacity, iter(weights))).solution
