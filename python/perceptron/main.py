from itertools import cycle
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

class Perceptron:
    """
        Perceptron test 1

        train_data: A 4x2 matrix with the input data

        target: A 4x1 matrix with the perceptron's excepted outputs

        lr: the learning rate. Defaults is 0.01

        inputs_nodes: the number of nodes in the input's layer of the perceptron.
            Should be equal to the second dimesion of train_data.
    """

def train(self):
    """
        Train a single layer perceptron
    """
    # The number of consecutive correct classifications
    correct_counter = 0

    for train, target in cycle(zip(self.train_data, self.target)):
        # end if all points are correctly classified
        if correct_counter == len(self.train_data):
            break

        output = self.classify(train)
        self.node_val = train

        if output == target:
            correct_counter += 1
        else:
            # if incorrectly classified, update weights and reset correct_counter
            self.update_weights(target, output)
            correct_counter = 0


def _gradient



train_data = np.array(
    [
        [0,0],
        [0,1],
        [1,0],
        [1,1]
    ]
)

target_xor = np.array(
    [
        [0],
        [1],
        [1],
        [0]
    ]
)

target_nand = np.array(
    [
        [1],
        [1],
        [1],
        [0]
    ]
)

target_or = np.array(
    [
        [0],
        [1],
        [1],
        [1]
    ]
)

target_and = np.array(
    [
        [0],
        [1],
        [1],
        [1]
    ]
)
