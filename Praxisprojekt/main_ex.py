from pipeline_ex import ETL
from analysis_ex import Analyser

figure_save_path = "C:\\Users\\user\\Dropbox\\DHBW Stuttgart\\Informatik 1 Python\\Projektarbeit_Wiessler\\venv\\vehicle_data_project_exercise\\"
pipeline = ETL("data_specs.json")
final_table = pipeline.run()
analyser = Analyser(final_table, figure_save_path=figure_save_path)
analyser.run()
