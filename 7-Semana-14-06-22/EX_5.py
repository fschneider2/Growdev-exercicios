# Qual foi o ano com maior gasto?

import os
os.system('clear')

from funcoes import importar_arquivo, dicionario_e_int

dados = importar_arquivo()
info = dicionario_e_int(dados)

ano = []
soma = []

for i in info:
    if i['ano'] not in ano:
        ano.append(i['ano'])
        soma.append([i['compra'], i['ano']]) #
    else:
        for j in soma:
            if j[1] == i['ano']:
                j[0] += i['compra']

print(max(soma))