# %%
import pandas as pd
import numpy as np
df = pd.read_csv("../data/clientes.csv", sep=";")

df.head()
# %%
# A Serie permite fazer uma conta aritimética da Serie com um escalar
df["qtdePontos"] + 100
# %%
df["pontos_100"] = df["qtdePontos"] + 100
df.head()

# %%
df["emailTwitch"] = df["flEmail"] + df["flTwitch"]
df.head()
# %%
df["email_ou_twitch"] = df["flEmail"] * df["flTwitch"]
#%%

df["qtdeSocial"] = df["flEmail"] + df["flTwitch"] + df["flYouTube"] + df["flBlueSky"] + df["flInstagram"]
df
# %%
## Verifico se a pessoa tem todas as redes sociais
df["todas_social"] = df["flEmail"] * df["flTwitch"] * df["flYouTube"] * df["flBlueSky"] + df["flInstagram"]
df

# %%
df["qtdePontos"].describe()
# %%

np.log(df["qtdePontos"]+1)
# %%
