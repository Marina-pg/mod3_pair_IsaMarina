from src import soporte as sp


df_clientes = sp.pd.read_csv("../files/clientes.csv", index_col=0)
df_ventas = sp.pd.read_csv("../files/ventas.csv", index_col=0)
df_productos = sp.pd.read_csv("../files/productos.csv", delimiter=",", index_col=0)
print("Descarga de csv´s")