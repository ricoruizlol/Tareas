import pandas as pd

datos={
    "nombres":["Maria", "luis", "Carmen"],
    "materias":["matematicas", "Programacion", "Mercadotecnia"],
    "promedios":[80,90,100],
}
df_alumnos = pd.DataFrame(datos)
print(df_alumnos)

pd.read