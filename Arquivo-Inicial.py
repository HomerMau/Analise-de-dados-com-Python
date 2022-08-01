#Passo 1:Importar a base de dados
import pandas as pd

tabela = pd.read_csv("telecom_users.csv")
print(tabela)

# Passo 2: Visualzar base de dados
# Entenderas informaçoes que voce tem dísponivel
# Resolver as besteiras na base de dados


# Escluir coluna inútil
tabela = tabela.drop("Unnamed: 0", axis=1)
print(tabela)



# Tratamento de dados
# Resolver as besteiras na base de dados
# Informaçoes do tipo correto
# Informaçoes Vazias