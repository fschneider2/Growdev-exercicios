# Qual foi o gasto por ano?

import os
os.system('clear')

from funcoes import importar_arquivo, dicionario_e_int,converter_RS

dados = importar_arquivo()
info = dicionario_e_int(dados)

ano = []
soma = []
# Pensei nessa logica, porém ela foi colocada em pratica e desenvolvida com o auxilio dos colegas Diego, Daniel e Alexson, em Grupo de estudos.
for i in info:
    if i['ano'] not in ano: # percorrendo o dicionario, salvando uma lista com os anos base, para ter comparativo 
        ano.append(i['ano'])
        soma.append([i['ano'], i['compra']]) # salvando a informação ano e compra, onde, se o ano ainda não foi adicionado a lista ano, ele ira adicionar uma unica vez.
    else:                                      # não esquecer de que, quando trabalhado com dicionario, colocar as info entre [] como no soma.append
        for j in soma: # percorrendo a lista soma
            if j[0] == i['ano']: # se se o ano já estiver la ele soma a informação de compra
                j[1] += i['compra']
soma.sort() # deixando o resultado em ordem crescente de anos

print('+','-'*45,'+')
for i in soma:
    val = converter_RS(i[1]) # para printar a resposta final
    print(f'| No ano {i[0]} foi gasto o total de {val} |')
print('+','-'*45,'+')










