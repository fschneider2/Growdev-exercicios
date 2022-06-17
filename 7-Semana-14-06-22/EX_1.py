# Procure quem foi a pessoa que mais gastou?

import os
os.system('clear')

from funcoes import dicionario_e_int, importar_arquivo

maior_compra = -1
indice_maior_compra = 0

dados = importar_arquivo() #função para importar os arquivos da lista
info = dicionario_e_int(dados) #função para converter dados necessarios em inteiros e adiciona-los a um dicionario.

for indice, linha in enumerate(info): # percorrendo o indice e a linha do arquivo, para que eu possa pegar o indice(posição) em que esta a maior compra e depois dar um print disso
    if linha['compra'] > maior_compra:
        maior_compra = linha['compra']
        indice_maior_compra = indice

pessoa = info[indice_maior_compra]

print('+','-'*69,'+')
print(f"| O Cliente que mais comprou foi: {pessoa['nome']} {pessoa['sobrenome']}                       |")
print(f"| A compra foi realizada em {pessoa['ano']}, paga no {pessoa['pagamento']} e com total de R$ {pessoa['compra']} |")
print('+','-'*69,'+')
