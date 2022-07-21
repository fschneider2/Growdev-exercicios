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
        repeticoes.append([1, i['sobrenome']]) # aqui, desenvolvemos uma logica muito interessante, com o auxilio do Diego Felipe
        sobrenomes.append(i['sobrenome']) # è adicionado um contador a frente de cada sobrenome, na mesma logica usada no ex_4
    else:
        for j in repeticoes:
            if j[1] == i['sobrenome']: 
                j[0] += 1 # se o sobrenome ja consta na lista, ele so soma o contador
a = max(repeticoes)


print('+','-'*62,'+')
print(f'| O Sobrenome que mais aparece é {a[1]}, presente em {a[0]} clientes |') # assim foi possivel identificar o mais presente.
print('+','-'*62,'+')