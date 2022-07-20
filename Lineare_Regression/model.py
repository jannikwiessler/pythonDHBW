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
        x = np.concatenate((vec_1, vec_2), axis=1)
        return np.matmul(x, self.theta)