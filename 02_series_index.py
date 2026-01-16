#%%
import pandas as pd

idades = [
    32,38,30,30,31,
    35,25,29,31,37,
    27,23,36,33,39
]

series_idades = pd.Series(idades)
series_idades
# %%
idades[0]
idades[-1]
# %%
## 'As series são parecidas com um dicionario de dados [chave e valor]'
series_idades[2]
# %%
series_idades = series_idades.sort_values()
series_idades
# %%
# indece de posição
series_idades.iloc[0]
# %%
series_idades.iloc[-1]
# %%
series_idades.iloc[:3]

# %%
idades = [
    32,38,30,30,31,
    35,25,29,31,37,
    27,23,36,33,39
]

indexs = [
    "Téo","Maria","Jose","Luis","Ana",
    "Nah","Dani","Mah","Fer","Nanda",
    "Patrick","Nih","Pedro","Kozato","Kozato"
]

series_idades = pd.Series(idades, index=indexs)
series_idades

# %%
series_idades[["Kozato"]]

## iloc = Navegar nas linhas
## loc = navegar nos indexs

# %%
