from import_data_ex import DataLoader
import pandas as pd


class ETL:
    final_table = pd.DataFrame()

    def __init__(self, data_specs=None):
        self.importer = DataLoader(data_specs)
        self.load_data()

    def run(self):
        self.enhance_raw_data()
        self.create_final_table()
        self.save_final_table()
        return self.final_table

    def save_final_table(self):
        database_path = self.importer.database_config["database_path"]
        # your code here #

    def create_final_table(self):
        self.raw_data_tables["sales_codes"] = self.raw_data_tables["sales_codes"].drop(columns=['Unnamed: 0'])
        self.raw_data_tables["vehicle_hash"] = self.raw_data_tables["vehicle_hash"].drop(
            columns=['Unnamed: 0', 'record_source', 'load_ts'])
        # your code here #

    def enhance_raw_data(self):
        self.handle_nans()
        self.handle_invalid_fins()
        self.handle_invalid_dates()

    def handle_invalid_dates(self):
        # your code here #
        pass

    def handle_invalid_fins(self, num_of_digits_in_fin=17):
        # your code here #
        pass

    def handle_nans(self):
        # your code here #
        pass

    def load_data(self):
        self.raw_data_tables = self.importer.load_data()
