import pyperf
from os import listdir
from os.path import isfile, join, basename
from macpacking.reader import BinppReader
from macpacking.model import Online, Offline
from macpacking.algorithms.online import NextFit as NextFitOn, FirstFit, BestFit, WorstFit, RefinedFirstFit
from macpacking.algorithms.offline import NextFit as NextFitOff, FirstFitDecreasing, BestFitDecreasing, WorstFitDecreasing
from macpacking.algorithms.baseline import BenMaier
from macpacking import WeightSet


def all_cases():
    return [
        './_datasets/binpp/N4C1W1/N4C1W1_A.BPP.txt',
        './_datasets/binpp/N1C3W1/N1C3W1_A.BPP.txt',
        './_datasets/binpp/N1C1W4/N1C1W4_A.BPP.txt',
        # './_datasets/binpp/N4C3W4/N4C3W4_A.BPP.txt',
    ]


def get_case_name(case: str) -> str:
    return basename(case).strip(".txt")


def get_case_data(case: str) -> WeightSet:
    return BinppReader(case).offline()


def all_online() -> list[Online]:
    return [NextFitOn(), FirstFit(), BestFit(), WorstFit(), RefinedFirstFit()]


def all_offline() -> list[Offline]:
    return [NextFitOff(), FirstFitDecreasing(), BestFitDecreasing(), WorstFitDecreasing(), BenMaier()]


def get_algo_name(obj) -> str:
    return f"{type(obj).__name__}_{type(obj).__mro__[1].__name__}"


def make_bench_name(case: str, obj) -> str:
    return f"{case}_{get_algo_name(obj)}"


def main():
    runner = pyperf.Runner()
    for algorithm in all_online() + all_offline():
        for case in all_cases():
            name = get_case_name(case)
            data = get_case_data(case)
            bench_name = make_bench_name(name, algorithm)
            runner.bench_func(bench_name, algorithm, data)


if __name__ == "__main__":
    main()
