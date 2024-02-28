import pandas as pd
import numpy as np
# cargar data
pollutant_data_frame = pd.read_csv("dataset.csv")

#Calcular los duplicados
duplicates_count = pollutant_data_frame.duplicated().sum()

print("Duplicados", duplicates_count)

distance_to_source = pollutant_data_frame["distance_to_source"]

pollutant_concentration = pollutant_data_frame["pollutant_concentration"]

pollutant_data_frame["pollutant_concentration"] = pollutant_data_frame["pollutant_concentration"].fillna(pollutant_data_frame["pollutant_concentration"].min())
pc_max = pollutant_data_frame["pollutant_concentration"].fillna(pollutant_data_frame["pollutant_concentration"].max())
pc_mean = pollutant_data_frame["pollutant_concentration"].fillna(pollutant_data_frame["pollutant_concentration"].mean())

print("Values Variable: ", pollutant_concentration)
print("Values Dataframe: ", pollutant_data_frame["pollutant_concentration"] )
print("Values MAX: ", pc_max)
print("Values MEAN: ", pc_mean)


missing_values_pc = pollutant_concentration.isnull().sum()
missing_values_pc_df = pollutant_data_frame["pollutant_concentration"].isnull().sum()


print("Missing Values: ", missing_values_pc)
print("Missing Values: ", missing_values_pc_df)
