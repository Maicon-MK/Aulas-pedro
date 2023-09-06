# Para abri os arquivos em exel
import pandas as pd
from twilio.rest import Client

# Passo a passo de solução
# Abri os arquivos em Excel
# Para cada arquivo:
# Verificar se algum valor na coluna vendas da daquele arquivo e maior que 55.000

# Se for maior que 55.000 envia um sms com o nome o mes eas vendas  do vendedor.

account_sid = "ACe56a63e9073fd86b9b5822437ccf0f61"
# Your Auth Token from twilio.com/console
auth_token = "f572f7ebed37231e05457be572b885ad"
# Variavel       #Lista
lista_meses = ["janeiro", "fevereiro", "março", "maio", "junho"]
# Para abri os arquivos Excel

# Para cada mes em listameses:
for mes in lista_meses:
    tabela_vendas = pd.read_excel(f"{mes}.xlsx")

    if (tabela_vendas["Vendas"] > 55000).any():
        vendas = tabela_vendas.loc[tabela_vendas["Vendas"] > 55000, "Vendas"].values[0]
        vendedor = tabela_vendas.loc[
            tabela_vendas["Vendas"] > 55000, "Vendedor"
        ].values[0]
        print(
            f"No mes {mes} alguem bateu a meta! Vendedor: {vendedor} Vendas: {vendas}"
        )

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+5521969898442",
    from_="+12569987631",
    body=f"No mes {mes} alguem bateu a meta! Vendedor: {vendedor} Vendas: {vendas}",
)

print(message.sid)
