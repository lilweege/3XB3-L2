from ... import Solution
from ...model import OfflineConstantBins as Offline
from ..capacity.online import FirstFit


class Greedy(Offline):

    def _process(self, num_bins: int, weights: list[int]) -> Solution:
        bins: Solution = [[] for _ in range(num_bins)]
        total_weights: list[int] = [0] * num_bins

        weights = sorted(weights, reverse=True)
        for weight in weights:
            min_idx = min(enumerate(total_weights), key=lambda x: x[1])[0]
            bins[min_idx].append(weight)
            total_weights[min_idx] += weight

        return bins


class MultiFit(Offline):

    def __init__(self, iterations=10):
        self.iterations = iterations

    def _process(self, num_bins: int, weights: list[int]) -> Solution:
        total_weights = sum(weights)
        max_weight = max(weights)

        lower_bound = int(max(total_weights/num_bins, max_weight))
        upper_bound = int(max(total_weights/num_bins*2, max_weight))

        sorted_items = sorted(weights, reverse=True)
        for _ in range(self.iterations):
            capacity = int((lower_bound + upper_bound) // 2)
            ffd_num_bins = FirstFit()((capacity, iter(sorted_items))).num_bins

            if ffd_num_bins <= num_bins:
                upper_bound = capacity
            else:
                lower_bound = capacity

        return FirstFit()((upper_bound, iter(sorted_items))).solution
