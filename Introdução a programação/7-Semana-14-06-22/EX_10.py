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
        if i['ano'] not in ano: # vejá que não foi possivel fazer isso: "if i['ano'] not in ano and i['sexo'] == 'M' and i['pagamento'] == 'credito':" apresentava um erro de calculo.
            repeticoes.append([1, i['ano']]) # utilizada a bese do EX-9, alterando informações e add os comparativos de sexo e forma de pagamento. 
            ano.append(i['ano'])
        else:
            for j in repeticoes:
                if j[1] == i['ano']:
                    j[0] += 1

a = max(repeticoes)

print('+','-'*76,'+')
print(f'| O ano que os homens mais utilizaram a função credito foi {a[1]}, em {a[0]} compras |')
print('+','-'*76,'+')