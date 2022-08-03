#Passo 1:Importar a base de dados
import pandas as pd

tabela = pd.read_csv("telecom_users.csv")
print(tabela)

# Passo 2: Visualzar base de dados
# Entenderas informaçoes que voce tem dísponivel
# Resolver as besteiras na base de dados


# Escluir coluna inútil
# axis = 0 eixo da linha
# axis = 1 eixo da coluna
tabela = tabela.drop("Unnamed: 0", axis=1)
print(tabela)



# Tratamento de dados
# Resolver as besteiras na base de dados
# Informaçoes do tipo correto
tabela["TotalGasto"] = pd.to_numeric(tabela["TotalGasto"], errors="coerce")

# Informaçoes Vazias
print(tabela.info())