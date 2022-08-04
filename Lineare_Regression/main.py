import os
from data_class import LinearRegressionData
from model import LinearRegressionModel
from optimizer import Optimizer

if __name__ == "__main__":
    linear_regression_data = LinearRegressionData({"feature": "T3", "target": "T4"},
                                                  os.path.join(os.getcwd(), "data.csv"))
    linear_regression_model = LinearRegressionModel(data=linear_regression_data)
    linear_regression_model.show_costs()
    linear_regression_model.set_theta((0, 0))
    linear_regression_model.show_training_data()
    optimizer = Optimizer(learning_rate=9e-6, max_iters=int(1e4))
    optimizer.train(model=linear_regression_model)
    optimizer.show_train_results()
    linear_regression_model.show_training_data()