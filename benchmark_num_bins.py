import pyperf
from os.path import basename
from macpacking.reader import BinppReader
from macpacking.model import Online, Offline
from macpacking.algorithms.num_bins.offline import Greedy, MultiFit
from macpacking.algorithms.num_bins.baseline import BenMaier
from macpacking import WeightSet


def all_cases():
    return ['./_datasets/binpp/N4C3W4/N4C3W4_A.BPP.txt']


def all_num_bins():
    return [100, 200, 400]


def get_case_name(case: str) -> str:
    return basename(case).strip(".txt")


def get_case_data(case: str) -> WeightSet:
    return BinppReader(case).offline()


def all_online() -> list[Online]:
    return []


def all_offline() -> list[Offline]:
    return [Greedy(), MultiFit(), BenMaier()]


def get_algo_name(obj) -> str:
    return f"{type(obj).__name__}_{type(obj).__mro__[2].__name__}"


def make_bench_name(case: str, obj) -> str:
    return f"{case}_{get_algo_name(obj)}"


def main():
    runner = pyperf.Runner()
    for algorithm in all_online() + all_offline():
        for num_bins in all_num_bins():
            for case in all_cases():
                name = get_case_name(case)
                data = (num_bins, get_case_data(case)[1])
                bench_name = make_bench_name(name, algorithm)
                runner.bench_func(bench_name + f"_{num_bins}", algorithm, data)


if __name__ == "__main__":
    main()
