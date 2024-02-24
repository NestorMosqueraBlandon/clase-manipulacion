import pandas as pd

# Importar o cargar data
df = pd.read_csv("dataset.csv")

duplicates_count = df.duplicated().sum()

"""
El set de datos no tiene duplicados
""" 

# Revisar que valores faltantes hay en que columna
missing_values_count = df.isnull().sum()
#print("Valores faltantes", missing_values_count)

pollutant = df["pollutant_concentration"]

df["pollutant_concentration"] = pollutant.fillna(pollutant.mean())

missing_values_count_two = df.isnull().sum()
#print("Valores faltantes", missing_values_count_two)

df_cleaned = df.dropna()

missing_values_count_three = df_cleaned.isnull().sum()
print("Valores faltantes", missing_values_count_three)

df_cleaned.to_csv("dataset_cleaned", index=False)
