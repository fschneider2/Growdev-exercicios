# Exiba o valor total de compras por modo de pagamento.

from funcoes import importar_arquivo, dicionario_e_int
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

dados = importar_arquivo()
info = dicionario_e_int(dados)

#Dados
credito = 0
debito = 0
dinheiro = 0

for i in info:
    if i['pagamento'] == 'credito':
        credito += 1
    elif i['pagamento'] == 'debito':
        debito += 1
    else:
        dinheiro += 1

# Grafico 

app = Dash(__name__)

df = pd.DataFrame({
    "modo de pagamento": ["Credito","Debito","Dinheiro"],
    "valores": [credito, debito, dinheiro]   
})

fig = px.pie(df, names="modo de pagamento", values="valores", color="modo de pagamento")
fig.update_traces(textposition='inside', textinfo='percent+value+label')

app.layout = html.Div(children=[
    html.H1(children='Comparativo de uso / formas de pagamento'),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
