# Utilize as seguintes faixas etárias nos exercícios em que for necessário.
# ● Jovens, 18 a 25 anos
# ● Adultos, 26 a 59 anos
# ● Idosos, igual ou maior que 60 anos

# Utilizando as faixas etárias, diga quantas pessoas há em cada faixa?

import os
os.system('clear')

from funcoes import importar_arquivo, dicionario_e_int

dados = importar_arquivo()
info = dicionario_e_int(dados)

jovens = 0
adultos = 0
idosos = 0

for i in info:
    if i['idade'] <= 25:
        jovens += 1

    elif i['idade'] <= 59:
        adultos += 1

    else:
        idosos += 1

total = jovens + adultos + idosos

print('+','-'*19,'+')
print(f'| Total clientes: {total}|\n| Jovens:          {jovens}| \n| Adultos:        {adultos}| \n| Idosos:          {idosos}|')
print('+','-'*19,'+')
