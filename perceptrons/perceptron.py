from typing import Tuple


class Perceptron:
    def __init__(self, dimension: int, learning_rate: float):
        self.weights = [1] + [0.01] * (dimension)
        self.learning_rate = learning_rate

    def train(self, x: Tuple[float, ...], target: int) -> None:
        x = (1,) + x  # add bias
        y = self.r_function(x)
        target_difference = target - y
        if target_difference != 0:
            weight_updates = [self.learning_rate * target_difference * x_i for x_i in x]
            self.weights = [self.weights[i] + weight_updates[i] for i in range(len(self.weights))]

    def r_function(self, x: Tuple[float, ...]) -> int:
        y = self.aggregation(x)
        y = self.activation(y)
        return y

    def aggregation(self, x: Tuple[float, ...]) -> float:
        return sum(x[i] * self.weights[i] for i in range(len(x)))

    def activation(self, x: float) -> int:
        return 1 if x > 0 else 0
