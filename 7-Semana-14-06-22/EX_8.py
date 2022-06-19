# A opção de débito é mais utilizada entre homens ou mulheres?

import os
os.system('clear')

from funcoes import importar_arquivo, dicionario_e_int

dados = importar_arquivo()
info = dicionario_e_int(dados)

m = 0
f = 0

for i in info:
    if i['sexo'] == 'M' and i['pagamento'] == 'debito': # utilizei comparativos e contadores 
        m += 1
    elif i['sexo'] == 'F' and i['pagamento'] == 'debito':
        f += 1

if m > f:
    mensagem = f'| A opção de débito é mais utilizada por homens, sendo usada {m} vezes por homens, contra {f} vezes por mulheres |'
else:
    mensagem = f'| A opção de débito é mais utilizada por mulheres, sendo usada {f} vezes por mulheres, contra {m} vezes por homens |'
print('+','-'*110,'+')
print(mensagem)
print('+','-'*110,'+')