import matplotlib.pyplot as plt
import pandas as pd


class Analyser:
    def __init__(self, table, figure_save_path):
        self.figure_save_path = figure_save_path
        self.final_table = table
        self.filter_for_years()

    def run(self):
        self.visualize_sales_per_countries()
        self.visualize_sales_per_year()

    def filter_for_years(self):
        df = self.final_table
        df["counter"] = 1
        # your code here #

    def visualize_sales_per_countries(self):
        # your code here #
        pass

    def visualize_sales_per_year(self):
        # your code here #
        pass