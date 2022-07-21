# Exiba um gráfico que mostre a quantidade total de compras agrupadas por anos.
from funcoes import importar_arquivo, dicionario_e_int
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

dados = importar_arquivo()
info = dicionario_e_int(dados)

repeticoes = []
ano = []

for i in info:
    if i['ano'] not in ano:
        repeticoes.append([i['ano'],1])
        ano.append(i['ano'])
    else:
        for j in repeticoes:
            if j[0] == i['ano']: 
                j[1] += 1

repeticoes.sort()

app = Dash(__name__)

df = pd.DataFrame({
    'anos': [y[0] for y in repeticoes],
    'total de compras': [s[1] for s in repeticoes]
})

fig = px.bar(df, x='anos', y='total de compras', text_auto=True)

app.layout = html.Div(children=[
    html.H3(children='''
      Total de compras por ano.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
