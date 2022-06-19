# Exiba um gráfico que mostre a quantidade total de compras agrupadas por anos.
from funcoes import importar_arquivo, dicionario_e_int
# import os
# os.system('clear')

dados = importar_arquivo()
info = dicionario_e_int(dados)


# Enunciado:
# 2) Exiba um gráfico que mostre a quantidade total de compras
# agrupadas por anos.

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

# chamada da funcao de leitura de arquivo

total_sales_for_year = []
years = []

for data in info:
    if data['ano'] in years:
        for j in total_sales_for_year:
            if j[0] == data['ano']:
                j[1] += data['compra']
    else:
        years.append(data['ano'])
        total_sales_for_year.append([data['ano'], data['compra']])

total_sales_for_year.sort()


app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame({
    "ano": [y[0] for y in total_sales_for_year],
    "valores": [s[1] for s in total_sales_for_year]
    
})

fig = px.bar(df, x="ano", y="valores")
fig.update_traces(textposition='inside', textinfo='percent+value+label')
app.layout = html.Div(children=[
    html.H1(children='Comparativo de quantidade de Homens e Mulheres'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)