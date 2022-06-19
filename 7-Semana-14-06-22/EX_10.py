# Qual foi o ano em que os homens mais usaram o crédito?

import os
os.system('clear')

from funcoes import importar_arquivo, dicionario_e_int

dados = importar_arquivo()
info = dicionario_e_int(dados)

repeticoes = []
ano = []

for i in info:
    if i['sexo'] == 'M' and i['pagamento'] == 'credito':
        if i['ano'] not in ano:
            repeticoes.append([1, i['ano']])
            ano.append(i['ano'])
        else:
            for j in repeticoes:
                if j[1] == i['ano']:
                    j[0] += 1

print(max(repeticoes))