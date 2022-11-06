import pytest
from macpacking.reader import BinppReader
from macpacking.algorithms.capacity.online import NextFit as NextFitOn, \
    FirstFit, BestFit, WorstFit, RefinedFirstFit
from macpacking.algorithms.capacity.offline import NextFit as NextFitOff, \
    FirstFitDecreasing, BestFitDecreasing, WorstFitDecreasing
from macpacking import Solution


@pytest.fixture
def binpp_input():
    return BinppReader('_datasets/binpp/N4C3W4/N4C3W4_A.BPP.txt').offline()


@pytest.fixture
def binpphard_input():
    return BinppReader('_datasets/binpp-hard/HARD0.BPP.txt').offline()


@pytest.fixture
def all_cases(binpp_input, binpphard_input):
    return [binpp_input, binpphard_input]


def is_solution_valid(capacity: int, solution: Solution):
    print(solution)
    return all(sum(weights) <= capacity for weights in solution)


@pytest.mark.parametrize("algorithm", [
    NextFitOn, FirstFit, BestFit, WorstFit, RefinedFirstFit, NextFitOff,
    FirstFitDecreasing, BestFitDecreasing, WorstFitDecreasing])
def test_algorithms(algorithm, all_cases):
    for case in all_cases:
        strategy = algorithm()
        solution = strategy(case).solution
        assert is_solution_valid(case[0], solution)
