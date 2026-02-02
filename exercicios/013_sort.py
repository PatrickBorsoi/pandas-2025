# %%

import pandas as pd

clientes = pd.read_csv("../data/clientes.csv", sep=";")

# Ordenando o top 5 do Maior para o menor em qtdePontos
clientes.sort_values(by="qtdePontos", ascending=False).head(5)
# %%
# Boa pratica que normalmente utilizam
top_5 = (clientes.sort_values(by="qtdePontos", ascending=False)
        .head(5)["idCliente"])
# %%

#exemplo se tiver um empate

brinquedo = pd.DataFrame(
    {
        "nome": ["Teo", "ana", "nah", "jose"],
        "idade": [32,43,35,42],
        "salario": [2345,4533,3245, 4533]
    }
)
brinquedo
# %%
brinquedo.sort_values(by=["salario", "idade"], ascending=[False, True])
# %%
