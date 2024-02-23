#PANDAS
#Libreria para manipulación de datos
#Seba en SERIES y DATAFRAMES
#DATAFRAMES Es una estructura de datos bidimensional consiste en Filas y Columnas, es similar a Excel

#name  age  gender => Representa observación
#Kathe  26    F => Representa variables 
#Mari   28    F => Representa variables
#Carlos diez  M
#Andrea casa  F

#name  age  gender => Representa observación
#Kathe  26    F => Representa variables 
#Mari   28    F => Representa variables
#Carlos 10    M
#Andrea casa  F


#outliers => Valor atipico

import pandas as pd

#Importar data
# data = pd.read_excel("data_huella.xlsx")

#Exportar data
# data.to_excel("data_huella_limpia.xlsx")


# DETECCIÓN Y ELIMINACIÓN DE DUPLICADOS

#Importar la data
df = pd.read_csv("data_pollutant.csv")

#Calcular el total de duplicados
duplicates_count = df.duplicated().sum()
print(df)
print("Cantidad de registros duplicados", duplicates_count)

#Elimnar los registros duplicados del DataFrame
df_cleaned = df.drop_duplicates()
print(df_cleaned)

df_cleaned.to_csv("data_pollutant_cleaned.csv", index=False)

#MIRAR VALORES FALTANTES
missing_values_count = df.isnull().sum()
print("Missing values: ", missing_values_count)

#Imputar datos
df_missing_imputed = df.fillna(df["distance_to_source"].mean())
