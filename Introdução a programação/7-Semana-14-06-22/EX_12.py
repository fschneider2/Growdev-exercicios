# Utilize as seguintes faixas etárias nos exercícios em que for necessário.
# ● Jovens, 18 a 25 anos
# ● Adultos, 26 a 59 anos
# ● Idosos, igual ou maior que 60 anos

# Qual o valor gasto em compras por jovens do ano de 2010 até 2015?

import os
os.system('clear')

from funcoes import importar_arquivo, dicionario_e_int, converter_RS

compra_2010_2015 = 0

c = 0

dados = importar_arquivo()
info = dicionario_e_int(dados)

for i in info:
    if i['idade'] <= 25 and i['ano'] >= 2010 and i['ano'] <= 2015: 
        compra_2010_2015 += i['compra']
        c += 1
        
compra_2010_2015 = converter_RS(compra_2010_2015)

print('+','-'*93,'+')
print(f'| Foram realizadas {c} compras por jovens entre 2010 e 2015. o Valor total é de R$ {compra_2010_2015} |')
print('+','-'*93,'+')