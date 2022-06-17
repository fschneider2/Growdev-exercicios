# Qual foi o gasto por ano?

import os
os.system('clear')

from funcoes import importar_arquivo, dicionario_e_int

dados = importar_arquivo()
info = dicionario_e_int(dados)

gastos_ano = {}

for i in info:
    ano = i['ano']
    gasto = i['compra']






