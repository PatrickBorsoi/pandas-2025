# %%
import pandas as pd

df = pd.read_csv("../data/clientes.csv", sep=";")
df.info()
# %%
## Converte o tipo da coluna
df["qtdePontos"].astype(int)

# %%
# Substitui datas inválidas antes de converter para datetime (boa prática)
replace = {"0000-00-00 00:00:00.000" : "2024-02-01 09:00:00.000"}

# Converte a coluna DtCriacao para datetime após tratar valores inválidos
df["DtCriacao"] = pd.to_datetime(df["DtCriacao"].replace(replace))
# %%
## É necessário converter para datetime para conseguir usar a função dt
# df["DtCriacao"].dt.year
# df["DtCriacao"].dt.month
# df["DtCriacao"].dt.month_name()
# df["DtCriacao"].dt.day
df["DtCriacao"].dt.date
