from ... import Solution
from ...model import OfflineConstantBins as Offline
import binpacking as bp


class BenMaier(Offline):

    def _process(self, num_bins: int, weights: list[int]) -> Solution:
        return bp.to_constant_bin_number(weights, num_bins)
