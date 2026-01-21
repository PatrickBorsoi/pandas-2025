#%%

import pandas as pd

df = pd.read_csv("../data/transacoes.csv", sep=";")

df
# %%
df.shape
# %%
df.info(memory_usage="deep")
# %%
df.dtypes
# %%
renamed_columns = {
    "QtdePontos":"qtPontos",
    "DescSistemaOrigem": "sistemaOrigem"
}


df.rename(columns=renamed_columns, inplace=True)
# %%
colunas = ["IdCliente",
           "qtPontos"]

df[colunas]
# %%
df[["IdCliente", "qtPontos"]].head(5)
# %%
