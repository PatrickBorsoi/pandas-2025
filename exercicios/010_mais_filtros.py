# %%
import pandas as pd

df = pd.read_csv("../data/transacao_produto.csv", sep=";")
df
# %%
filtro = (df["IdProduto"] == '5') | (df["IdProduto"] == '11')
filtro 
df[filtro]
# %%
filtro = df["IdProduto"].isin(["5","11"])
df[filtro]
# %%    
clientes = pd.read_csv("../data/clientes.csv", sep=";")
clientes
# %%
#Tudo oque é NA

# filtro_na_clientes = clientes["DtCriacao"].isna()
# filtro_na_clientes
# df[filtro_na_clientes]

#Tudo que não é NA

# filtro_clientes = clientes["DtCriacao"].notna()
# filtro_clientes
# df[filtro_clientes]
# %%
# ~ = not
~clientes["DtCriacao"].isna()
# %%
