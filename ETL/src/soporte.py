import pandas as pd

def cambiar_a_unk(df,columnas):

    for c in columnas:
        try:
            df[c]= df[c].fillna('unknown')
        except:
            df[c]= df[c]

