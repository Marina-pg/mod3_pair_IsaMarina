from src import soporte as sp


df_clientes = sp.pd.read_csv("../files/clientes.csv", index_col=0)
df_ventas = sp.pd.read_csv("../files/ventas.csv", index_col=0)
df_productos = sp.pd.read_csv("../files/productos.csv", delimiter=",", index_col=0)
print("Descarga de csv´s")


lista_dfs = [df_clientes, df_ventas, df_productos]

for l in lista_dfs:
    sp.buscar_duplicados(l)
    print(f'Buscando duplicados en {l}')


sp.cambiar_a_unk(df_clientes,df_clientes.columns)
print('cambio nulos por unknown en df_clientes')
