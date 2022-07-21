# Utilize as seguintes faixas etárias nos exercícios em que for necessário.
# ● Jovens, 18 a 25 anos
# ● Adultos, 26 a 59 anos
# ● Idosos, igual ou maior que 60 anos

# Qual é a faixa etária que mais gasta?

import os
os.system('clear')

from funcoes import importar_arquivo, dicionario_e_int, converter_RS

dados = importar_arquivo()
info = dicionario_e_int(dados)

jovens = 0
j = 0
adultos = 0
a= 0
idosos = 0
ido = 0

for i in info:
    if i['idade'] <= 25:
        jovens += i['compra']
        j += 1 # novamente contadores e comparativos, é possivel utilizar a mesma metodologia do ex_4, porém fiz esse antes de resolver aquela logica. 
    elif i['idade'] <= 59:
        adultos += i['compra']
        a += 1
    else:
        idosos += i['compra']
        ido += 1

jovens = converter_RS(jovens) # convertendo em R$
adultos = converter_RS(adultos)
idosos = converter_RS(idosos)

if jovens > adultos and jovens > idosos:
    mensagem = f'| A faixa etaria que mais gasta é a dos jovens, o total gasto por essa faixa etaria foi de R$ {jovens} |'
elif adultos > jovens and adultos > idosos:
    mensagem = f'| A faixa etaria que mais gasta é a dos adultos, o total gasto por essa faixa etaria foi de R$ {adultos} |'
else:
    mensagem = f'| A faixa etaria que mais gasta é a dos idosos, o total gasto por essa faixa etaria foi de R$ {idosos} |'

print('+','-'*39,'+')
print(f'|   Total de vendas       Valor vendas    |\n| Jovens:  {j} vendas    R$ {jovens}  | \n| Adultos: {a} vendas   R$ {adultos} | \n| Idosos:  {ido} vendas    R$ {idosos}  |')
print('+','-'*39,'+')

print('+','-'*104,'+')
print(mensagem)
print('+','-'*104,'+')