# Qual a média de todas as notas (do 1º e 2º semestre) dos alunos do 2º ano?

from funcoes import importar_arquivo

import os

os.system('clear')

dados = importar_arquivo()

media_alunos = []

for i in dados:
    if i['ano'] == 2:
        media_alunos.append(i['media']) #codigo mais simples que consegui criar, como a média já esta dentro do dicionario proncipal, foi uma simples verificação do ano


media = sum(media_alunos) / len(media_alunos) # calculo da média de todas as notas dos alunos do 2° ano


print('Qual a média de todas as notas (do 1º e 2º semestre) dos alunos do 2º ano? \n')

print('Resposta:')
print('+','-'*47,'+')
print(f'| A média das notas dos alunos do 2° ano foi: {media:.3} |')
print('+','-'*47,'+')