from random import shuffle

from perceptrons.dataset import Dataset
from perceptrons.perceptron import Perceptron
from perceptrons.sigmoidal_perceptron import SigmoidalPerceptron


class Trainer:
    def __init__(self, perceptron: Perceptron, training_dataset: Dataset, test_dataset: Dataset, training_rounds: int):
        self.perceptron = perceptron
        self.training_data = training_dataset.data
        self.test_data = test_dataset.data
        self.training_rounds = training_rounds

    def train(self) -> None:
        keys = list(self.training_data.keys())
        for j in range(self.training_rounds):
            shuffle(keys)
            for x in keys:
                target = self.training_data[x]
                self.perceptron.train(x, target)

        correct = 0
        shuffle(keys)
        for x in keys:
            target = self.training_data[x]
            y = self.perceptron.r_function(x)
            if y == target:
                correct += 1
        print(f'last round: {correct / len(self.training_data) * 100}% accuracy')

    def test(self) -> float:
        correct = 0
        for x in self.test_data.keys():
            target = self.test_data[x]
            y = self.perceptron.r_function(x)
            if y == target:
                correct += 1
        return correct / len(self.test_data.keys())


class GradientDescentTrainer:
    def __init__(self, perceptron: SigmoidalPerceptron, training_dataset: Dataset, test_dataset: Dataset,
                 training_rounds: int, batch_size: int):
        self.perceptron = perceptron
        self.training_dataset = training_dataset
        self.test_data = test_dataset.data
        self.training_rounds = training_rounds
        self.batch_size = batch_size

    def train(self) -> None:
        for _ in range(self.training_rounds):
            self.perceptron.train(self.training_dataset, self.batch_size)

    def test(self) -> float:
        deviation_sum = 0
        for input in self.test_data.keys():
            target = self.test_data[input]
            y = self.perceptron.r_function(input)
            error = abs(target - y)
            deviation_sum += error
        return deviation_sum / len(self.test_data.keys())
