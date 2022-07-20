import os
import pandas as pd


class LinearRegressionData:
    def __init__(self, *args):
        self.raw_data: pd.DataFrame = pd.DataFrame()
        self.feature: dict = {"data": None, "name": None}
        self.target: dict = {"data": None, "name": None}
        self.number_of_samples: int = 0

        for arg in args:
            if isinstance(arg, str) and os.path.isfile(arg):
                self.raw_data = pd.read_csv(arg, delimiter=',')
            elif isinstance(arg, pd.DataFrame):
                self.raw_data = arg
            elif isinstance(arg, dict):
                if "feature" in arg.keys():
                    self.feature["name"] = arg["feature"]
                if "target" in arg.keys():
                    self.target["name"] = arg["target"]
            else:
                print("invalid type")

        self.feature["data"] = self.raw_data[self.feature["name"]]
        self.target["data"] = self.raw_data[self.target["name"]]
        self.number_of_samples = len(self.feature["data"])
