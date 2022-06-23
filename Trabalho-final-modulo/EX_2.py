# Quantos alunos do 1º ano foram aprovados sem exame?

from funcoes import importar_arquivo
import os

os.system('clear')

dados = importar_arquivo()

aprovados_sem_exame = 0

for i in dados:
    if i['ano'] == 1 and i['nota_exame'] == 0 and i['faltas'] <= 15: # Utilizado um laço de repetição, para percorrer a lista e contar a informação solicitada
            aprovados_sem_exame += 1

print('Quantos alunos do 1º ano foram aprovados sem exame?\n')

print('Resposta:')

print('+','-'*46,'+')
print(f'| {aprovados_sem_exame} alunos do 1° ano foram aprovados sem exame |')
print('+','-'*46,'+')

