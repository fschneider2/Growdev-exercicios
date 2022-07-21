# Exiba um gráfico que mostre a quantidade total de gastos com compras agrupadas por anos.

from funcoes import importar_arquivo, dicionario_e_int
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

dados = importar_arquivo()
info = dicionario_e_int(dados)

# dados para o grafico

soma = []
ano = []

for data in info:
    if data['ano'] in ano:
        for i in soma:
            if i[0] == data['ano']:
                i[1] += data['compra']
    else:
        ano.append(data['ano'])
        soma.append([data['ano'], data['compra']])

soma.sort() 

# Grafico
app = Dash(__name__)

df = pd.DataFrame({
    'anos': [y[0] for y in soma],
    'valores': [s[1] for s in soma]
})

fig = px.bar(df, x='anos', y='valores', text_auto=True)

app.layout = html.Div(children=[
    html.H3(children='''
      Total de gastos por anos.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
