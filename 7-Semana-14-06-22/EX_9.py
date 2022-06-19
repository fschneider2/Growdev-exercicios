# Qual o sobrenome que mais aparece na base de dados?

import os
os.system('clear')

from funcoes import importar_arquivo, dicionario_e_int

dados = importar_arquivo()
info = dicionario_e_int(dados)

repeticoes = []
sobrenomes = []

for i in info:
    if i['sobrenome'] not in sobrenomes:
        repeticoes.append([1, i['sobrenome']])
        sobrenomes.append(i['sobrenome'])
    else:
        for j in repeticoes:
            if j[1] == i['sobrenome']:
                j[0] += 1
print(max(repeticoes))
