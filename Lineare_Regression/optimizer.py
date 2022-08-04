import os
import numpy as np
import matplotlib.pyplot as plt
from data_class import LinearRegressionData
from model import LinearRegressionModel


class Optimizer:
    def __init__(self, learning_rate: float = 0.01, max_iters: int = 1e5):
        self.costs = []
        self.learning_rate = learning_rate
        self.max_iters = max_iters

    def train(self, model: LinearRegressionModel):
        x = np.matrix([np.ones(model.data.number_of_samples), model.data.feature["data"]])
        for i in range(self.max_iters):
            tmp = model.hypothesis() - np.matrix(model.data.target["data"]).T
            model.theta = model.theta - (self.learning_rate / model.data.number_of_samples) * np.matmul(x, tmp) # 2x98 * 98x1
            self.costs.append(model.costs())
        model.final_theta = (float(model.theta[0]), float(model.theta[1]))
        print(model.final_theta)

    def show_train_results(self):
        fig, ax = plt.subplots()
        ax.plot([i for i in range(self.max_iters)], self.costs)
        plt.show()


