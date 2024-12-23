import copy
from dataclasses import dataclass
from random import normalvariate, shuffle
from typing import Dict, List, Tuple


@dataclass
class Dataset:
    data: Dict[Tuple[float, ...], int]


class DatasetGenerator:
    def __init__(self, ideal_data: Dict[int, List[List[int]]], stddev: float = 0.01):
        self.ideal_data = ideal_data
        self.stddev = stddev

    def generate(self, size: int) -> Dataset:
        data = {}
        samples_per_entry = size // len(self.ideal_data.keys())
        for i in self.ideal_data.keys():
            for _ in range(samples_per_entry):
                new_digit = copy.deepcopy(self.ideal_data[i])
                noisy_digit = self.add_noise(new_digit)
                data[noisy_digit] = i
        return Dataset(data)

    def add_noise(self, digit: List[List[int]]) -> Tuple[float, ...]:
        noisy_digit = tuple(value + normalvariate(0, self.stddev) for row in digit for value in row)
        return noisy_digit

    @staticmethod
    def split(dataset: Dataset, training_percentage: float) -> Tuple[Dataset, Dataset]:
        split_index = int(len(dataset.data.keys()) * training_percentage)
        training_data, testing_data = {}, {}
        keys = list(dataset.data.keys())
        shuffle(keys)
        for i, key in enumerate(keys):
            if i < split_index:
                training_data[key] = dataset.data[key]
            else:
                testing_data[key] = dataset.data[key]
        return Dataset(training_data), Dataset(testing_data)
