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


tabela = tabela.dropna(how="all", axis=1)

# Linhas que tem alguma informação vazia
tabela = tabela.dropna(how="any", axis=0)

# Informaçoes Vazias
print(tabela.info())

# Analise inicial de Dados
# Como estão os cancelamentos? 26%
print(tabela["Churn"].value_counts())

print(tabela["Churn"].value_counts(normalize=True).map("{:.1%}".format))


# Descobrir os Motivos do Cancelamento

import plotly.express as px


for coluna in tabela.columns:
  # Etapa 1, Cria o Grafico
  # histograms

  grafico = px.histogram(tabela, x="Aposentado", color="Churn", text_auto=True)

  # Etapa 2, Exibe o grafico
  grafico.show()