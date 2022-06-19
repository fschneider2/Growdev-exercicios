# Qual a porcentagem de homens e mulheres na base de dados?

import os
os.system('clear')

from funcoes import importar_arquivo, dicionario_e_int

m = 0
f = 0

dados = importar_arquivo()
info = dicionario_e_int(dados)

for i in info: # percorrendo a lista
    if i['sexo'] == 'M': # filtrando os homens
        m += 1
    else: # filtrando as mulheres
        f += 1

per_m = (m * 100) / len(info) # calculando as %
per_f = 100 - per_m 

print('+','-'*62,'+')
print(f'| A base de dados possui {per_m} % de homens e {per_f} % de mulheres |')
print('+','-'*62,'+')