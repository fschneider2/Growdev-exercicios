# Qual foi o gasto por ano?

import os
os.system('clear')

from funcoes import importar_arquivo, dicionario_e_int, filtrar_anos

dados = importar_arquivo()
info = dicionario_e_int(dados)

ano = []
soma = []

for i in info:
    if i['ano'] not in ano:
        ano.append(i['ano'])
        soma.append([i['ano'], i['compra']]) #
    else:
        for j in soma:
            if j[0] == i['ano']:
                j[1] += i['compra']
soma.sort()

for i in soma:
    print(f'No ano {i[0]} foi gasto o total de {i[1]}')










