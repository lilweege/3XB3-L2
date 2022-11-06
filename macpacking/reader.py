from abc import ABC, abstractmethod
from random import shuffle, seed
from . import WeightSet, WeightStream
from .utils import check_file_exists


class DatasetReader(ABC):

    def offline(self) -> WeightSet:
        '''Return a WeightSet to support an offline algorithm'''
        (capacity, weights) = self._load_data_from_disk()
        seed(42)          # always produce the same shuffled result
        shuffle(weights)  # side effect shuffling
        return (capacity, weights)

    def online(self) -> WeightStream:
        '''Return a WeighStream, to support an online algorithm'''
        (capacity, weights) = self.offline()

        def iterator():  # Wrapping the contents into an iterator
            for w in weights:
                yield w  # yields the current value and moves to the next one

        return (capacity, iterator())

    @abstractmethod
    def _load_data_from_disk(self) -> WeightSet:
        '''Method that read the data from disk, depending on the file format'''
        pass


class BinppReader(DatasetReader):
    '''Read problem description according to the BinPP format'''

    def __init__(self, filename: str) -> None:
        check_file_exists(filename)
        self.__filename: str = filename

    def _load_data_from_disk(self) -> WeightSet:
        with open(self.__filename, 'r') as reader:
            nb_objects: int = int(reader.readline())
            capacity: int = int(reader.readline())
            weights: list[int] = [
                int(reader.readline()) for _ in range(nb_objects)
            ]
            return (capacity, weights)


class JBurkardtReader(DatasetReader):
    '''Read problem description according to the jburkardt format'''

    def __init__(self, capacity_filename: str, weights_filename: str) -> None:
        check_file_exists(capacity_filename)
        check_file_exists(weights_filename)
        self.__capacity_filename = capacity_filename
        self.__weights_filename = weights_filename

    def _load_data_from_disk(self) -> WeightSet:
        with open(self.__capacity_filename, 'r') as reader:
            capacity: int = int(reader.readline())
        with open(self.__weights_filename, 'r') as reader:
            weights: list[int] = list(map(int, reader.read().strip().split()))
        return (capacity, weights)
