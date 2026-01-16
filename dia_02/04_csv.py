#%%
import pandas as pd
import pyarrow

df = pd.read_csv("../data/clientes.csv",sep=";")

df
# %%

df.to_csv("../dia_02/clientes.csv", index=False)
# %%
df.to_parquet("../dia_02/clientes.parquet", index=False)
# %%
df_2 = pd.read_parquet("../dia_02/clientes.parquet")
df_2

# %%
df.to_excel("../dia_02/clientes.xlsx", index=False)


# %%
df_3 = pd.read_excel("../dia_02/clientes.xlsx")
df_3

# %%
