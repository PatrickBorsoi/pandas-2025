# %% 
import pandas as pd

df = pd.read_csv("../data/transacoes.csv",  sep=";")
df.head()
# %%

## filtrando somente com python
pontos = [10, 1, 1, 1, 50, 100, 23, 12,56, 30]

filtro = []
valores_50_mais = []

for i in pontos:
    filtro.append(i>=50)
filtro

resultado = []
for i in range(len(pontos)):
    if filtro[i]:
        resultado.append(pontos[i])
resultado
# %%

brinquedo = pd.DataFrame(
    {
        "nome": ["teo", "nah", "mah"],
        "idade": [32, 35, 14],
        "uf": ["sp", "pr", "rj"]
    }
)

# filtro
brinquedo[filtro]

# retorna uma Serie booleana
brinquedo["idade"] >= 18

# retorna o Dataframe
# brinquedo[brinquedo["idade"] >= 18]

# %%
filtro_bool = [False, True, True]

brinquedo[filtro_bool]


# %%
## Transações com mais de 50 pontos
df = pd.read_csv("../data/transacoes.csv",  sep=";")
df.head()

# %%
# valores maiores que 50
filtro = df["QtdePontos"] >= 50

df = df[pontos]
df 

# %%
# valoress entre 50 e 100
filtro = (df["QtdePontos"] >= 50) & (df["QtdePontos"] < 100)
df[filtro]
# %%
filtro = (df["QtdePontos"] == 1) | (df["QtdePontos"] == 100)

df[filtro]

# %%
filtro = (df["QtdePontos"] > 0) & (df["QtdePontos"] <= 50) & (df["DtCriacao"] >= "2025-01-01")
df[filtro]

# %%
# pontos entre 0 e 50 ou do ano de 2025 para frente

filtro = (df["QtdePontos"] > 0) & (df["QtdePontos"] <= 50) & ((df["DtCriacao"] >= "2025-01-01"))
df[filtro]
# %%
f = df["QtdePontos"]

for i in df["QtdePontos"]:
    [i]