from enum import Enum

from perceptrons.dataset import DatasetGenerator
from perceptrons.perceptron import Perceptron
from perceptrons.sigmoidal_perceptron import SigmoidalPerceptron
from perceptrons.trainer import Trainer, GradientDescentTrainer


class Mode(Enum):
    PERCEPTRON_HYPERPARAMETER_GRID_SEARCH = 1,
    SIGMOIDAL_PERCEPTRON_HYPERPARAMETER_GRID_SEARCH = 2,
    TEST_PERCEPTRON = 3,
    TEST_SIGMOIDAL_PERCEPTRON = 4


if __name__ == '__main__':
    ideal_data = {
        0: [
            [0, 1, 1, 0],
            [1, 0, 0, 1],
            [1, 0, 0, 1],
            [1, 0, 0, 1],
            [0, 1, 1, 0],
        ],
        1: [
            [0, 0, 1, 0],
            [0, 1, 1, 0],
            [0, 0, 1, 0],
            [0, 0, 1, 0],
            [0, 0, 1, 0],
        ]
    }

    dataset_generator = DatasetGenerator(ideal_data)
    mode = Mode.SIGMOIDAL_PERCEPTRON_HYPERPARAMETER_GRID_SEARCH

    match mode:
        case Mode.PERCEPTRON_HYPERPARAMETER_GRID_SEARCH:
            best_config = (0, 0, 0)
            highest_accuracy = 0
            for dataset_size in (100, 1_000, 10_000):
                for learning_rate in (0.1, 0.01, 0.001, 0.0001):
                    for training_rounds in (10, 100, 1000):
                        print(
                            f'training with dataset size={dataset_size}, learning rate={learning_rate}, training_rounds={training_rounds}')

                        dataset = dataset_generator.generate(dataset_size)
                        training_data, test_data = DatasetGenerator.split(dataset, 0.8)

                        dimension = 4 * 5
                        perceptron = Perceptron(dimension, learning_rate)
                        trainer = Trainer(perceptron, training_data, test_data, training_rounds)
                        trainer.train()
                        accuracy = trainer.test()

                        print(f'accuracy: {accuracy * 100}%\n')

                        if accuracy > highest_accuracy:
                            highest_accuracy = accuracy
                            best_config = (dataset_size, learning_rate, training_rounds)

            print(
                f'best config: dataset size={best_config[0]}, learning rate={best_config[1]}, training_rounds={best_config[2]} with an accuracy of {highest_accuracy * 100}%')
            # best config: dataset size=100, learning rate=0.001, training_rounds=1000 with an accuracy of 70.0%
            # best config: dataset size=1000, learning rate=0.001, training_rounds=100 with an accuracy of 56.00000000000001%
            # best config: dataset size=100, learning rate=0.0001, training_rounds=100 with an accuracy of 65.0%

        case Mode.SIGMOIDAL_PERCEPTRON_HYPERPARAMETER_GRID_SEARCH:
            best_config = (0, 0, 0, 0)
            lowest_stddev = 1
            # for dataset_size in (100, 1_000, 10_000):
            #     for learning_rate in (0.1, 0.01, 0.001, 0.0001):
            #         for training_rounds in (1, 10, 100, 1000):
            #             for batch_size in (1, 5, 10, 50, 100):
            for dataset_size in (100, 200, 500):
                for learning_rate in (0.005, 0.0001, 0.0005, 0.00001):
                    for training_rounds in (1, 10, 20, 50):
                        for batch_size in (1, 5, 10, 50, 100, 200):
                            print(
                                f'training with dataset size={dataset_size}, learning rate={learning_rate}, training_rounds={training_rounds}, batch_size={batch_size}')

                            dataset = dataset_generator.generate(dataset_size)
                            training_data, test_data = DatasetGenerator.split(dataset, 0.8)

                            dimension = 4 * 5
                            perceptron = SigmoidalPerceptron(dimension, learning_rate)
                            trainer = GradientDescentTrainer(perceptron, training_data, test_data, training_rounds,
                                                             min(batch_size, dataset_size))
                            trainer.train()
                            stddev = trainer.test()

                            print(f'standard deviation: {stddev}\n')

                            if stddev < lowest_stddev:
                                lowest_stddev = stddev
                                best_config = (dataset_size, learning_rate, training_rounds, batch_size)

            print(
                f'best config: dataset size={best_config[0]}, learning rate={best_config[1]}, training_rounds={best_config[2]}, batch_size={best_config[3]} with an standard deviation of {lowest_stddev}')
            # best config: dataset size=10000, learning rate=0.0001, training_rounds=10, batch_size=1 with an standard deviation of 0.44177669994157065

        case Mode.TEST_PERCEPTRON:
            dataset_size = 400
            learning_rate = 0.01
            training_rounds = 100

            dataset = dataset_generator.generate(dataset_size)
            training_data, test_data = DatasetGenerator.split(dataset, 0.8)

            dimension = 4 * 5
            perceptron = Perceptron(dimension, learning_rate)
            trainer = Trainer(perceptron, training_data, test_data, training_rounds)
            trainer.train()
            accuracy = trainer.test()

            print(f'accuracy: {accuracy * 100}%\n')

        case Mode.TEST_SIGMOIDAL_PERCEPTRON:
            dataset_size = 1000
            learning_rate = 0.01
            training_rounds = 1000
            batch_size = 50

            dataset = dataset_generator.generate(dataset_size)
            training_data, test_data = DatasetGenerator.split(dataset, 0.8)

            dimension = 4 * 5
            perceptron = SigmoidalPerceptron(dimension, learning_rate)
            trainer = GradientDescentTrainer(perceptron, training_data, test_data, training_rounds, batch_size)
            trainer.train()
            stddev = trainer.test()

            print(f'standard deviation: {stddev}\n')
