# Busque quais são os anos da base de dados?

import os
os.system('clear')

from funcoes import importar_arquivo, dicionario_e_int, filtrar_anos

dados = importar_arquivo()

info = dicionario_e_int(dados)

anos = filtrar_anos(info) # função para retornar uma lista, com os anos da base de dados, utilizei em outro exercicio, por isso a função.

print('+','-'*95,' +')
print(f'| A base de dados é composta de vendas realizadase entre {anos[0]} e {anos[-1]}                               |')
print('+','-'*95,' +')
print(f'| {anos} |')
print('+','-'*95,' +')
