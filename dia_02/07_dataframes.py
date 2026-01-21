#%%

import pandas as pd

df_clientes = pd.read_csv("../data/clientes.csv", sep=";")

df_clientes
# %%
df_clientes.head(20)
# %%
df_clientes.tail()
# %%
df_clientes.shape
# %%
df_clientes.columns
# %%
df_clientes.info(memory_usage="deep")
# %%
df_clientes.dtypes["idCliente"]
# %%
