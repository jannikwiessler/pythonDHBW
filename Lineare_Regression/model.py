import os.path
import numpy as np
import matplotlib.pyplot as plt
from data_class import LinearRegressionData
from mpl_toolkits.mplot3d import axes3d


class LinearRegressionModel:
    def __init__(self, data: LinearRegressionData):
        self.theta = (0, 0)
        self.final_theta = (0, 0)
        self.data = data

    def set_theta(self, theta: tuple = (0, 0)):
        self.theta = np.matrix([[theta[0]], [theta[1]]])

    def hypothesis(self):
        vec_1 = np.ones(self.data.number_of_samples).reshape(self.data.number_of_samples, 1)
        vec_2 = np.array(self.data.feature["data"]).reshape(self.data.number_of_samples, 1)
        A = np.concatenate((vec_1, vec_2), axis=1)
        return np.matmul(A, self.theta)

    def costs(self):
        error = self.hypothesis() - np.array(self.data.target["data"]).reshape(self.data.number_of_samples, 1)
        error_square = np.power(error, 2)
        return (sum(error_square) / (2 * self.data.number_of_samples))[0, 0]

    def show_costs(self):
        costs_list = []
        theta_0_values = np.arange(50, 150, 0.5)  # 200
        theta_1_values = np.arange(0, 2, 0.05)  # 40
        x, y = np.meshgrid(theta_0_values, theta_1_values)
        for theta_0, theta_1 in zip(x.flatten(), y.flatten()):
            self.set_theta((theta_0, theta_1))
            costs_list.append(self.costs())
        costs = np.array(costs_list).reshape(x.shape)
        fig = plt.figure()
        ax = plt.axes(projection='3d')
        ax.plot_surface(x, y, costs)
        plt.show()

    def show_training_data(self):
        self.set_theta(self.final_theta)
        fig, ax = plt.subplots()
        ax.scatter(x=self.data.feature['data'], y=self.data.target['data'])
        ax.plot(self.data.feature['data'], self.hypothesis(), 'r')
        plt.xlabel("T3")
        plt.ylabel("T4")
        plt.show()

