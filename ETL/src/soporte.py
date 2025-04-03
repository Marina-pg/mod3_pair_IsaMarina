import pandas as pd

def buscar_duplicados(df):
    print(f'Este DataFrame tiene {df.duplicated().sum()} filas duplicadas')

def cambiar_a_unk(df,columnas):

    for c in columnas:
        try:
            df[c]= df[c].fillna('unknown')
        except:
            df[c]= df[c]

