import math
from random import uniform, choice
from typing import Tuple

from perceptrons.dataset import Dataset


class SigmoidalPerceptron:
    def __init__(self, dimension: int, learning_rate: float):
        self.weights = [-1] + [uniform(-0.1, 0.1) for _ in range(dimension)]
        self.learning_rate = learning_rate

    def train(self, dataset: Dataset, batch_size: int) -> None:
        weight_updates = [0] * len(self.weights)
        for _ in range(batch_size):
            input_without_bias = choice(list(dataset.data))
            input = (1,) + input_without_bias
            target = dataset.data[input_without_bias]
            y = self.r_function(input)
            new_updates = [(target - y) * y * (1 - y) * x for x in input]
            weight_updates = [weight_updates[i] + self.learning_rate * new_updates[i]
                              for i in range(len(weight_updates))]
        self.weights = [self.weights[i] + weight_updates[i]
                        for i in range(len(self.weights))]

    def r_function(self, x: Tuple[float, ...]) -> float:
        y = self.aggregation(x)
        y = self.activation(y)
        return y

    def aggregation(self, x: Tuple[float, ...]) -> float:
        return sum(x[i] * self.weights[i] for i in range(len(x)))

    def activation(self, x: float) -> float:
        return 1 / (1 + math.exp(-x))
