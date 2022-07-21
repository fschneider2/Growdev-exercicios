# Qual foi o ano com maior gasto?

import os
os.system('clear')

from funcoes import importar_arquivo, dicionario_e_int, converter_RS

dados = importar_arquivo()
info = dicionario_e_int(dados)

ano = []
soma = []

for i in info: # mesmo codigo do exercicio 4
    if i['ano'] not in ano:
        ano.append(i['ano'])
        soma.append([i['compra'], i['ano']]) #porém, com as informações salvas em ordem diferente, primeiro o compras
    else:
        for j in soma:
            if j[1] == i['ano']:
                j[0] += i['compra']
a = max(soma) #criando uma variavel para conseguir apresentar separadamente os valores de ano e soma
val = converter_RS(a[0]) # convertendo o valor em R$ 

print('+','-'*86,'+')
print(f'| O ano de {a[1]} foi o que apresentou maior receita, com o valor total de R$ {val} |') # para que se possa utilizar a função max, e pegar o valor maximo das compras
print('+','-'*86,'+')