# %%
import pandas as pd

clientes = pd.read_csv("../data/clientes.csv", sep=";")
clientes
# %%
"""Da um erro, porque o clientes_0 esta associado a clientes, quando
se usa .copy() desassociamos
"""
filtro = clientes["qtdePontos"] == 0
clientes_0 = clientes[filtro]
clientes_0["flag_1"] = 1
# %%
filtro = clientes["qtdePontos"] == 0
clientes_0 = clientes[filtro].copy()
clientes_0["flag_1"] = 1
clientes_0
# %%
