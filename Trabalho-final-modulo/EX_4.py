# De todos os alunos que reprovaram quantos foram por falta e quantos foram por nota, e quantos foram por ambas as causas?

from funcoes import importar_arquivo

import os

os.system('clear')

dados = importar_arquivo()

alunos_reprovados = {'falta': 0, 'nota': 0, 'ambos': 0}

for i in dados: 
    if i['faltas'] > 15 and i['media'] < 7: # iniciamos a verificação e contagem pelo 'ambos', optei por fazer 3 laços de repetição, um para cada pergunta, entendi que o codigo ficou mais legivel desta forma.
        if i['nota_exame'] <= 5:
            alunos_reprovados['ambos'] += 1 

for i in dados: 
    if i['media'] < 7 and i['nota_exame'] < 5:
            alunos_reprovados['nota'] += 1 

for i in dados:
    if i['faltas'] > 15:
        alunos_reprovados['falta'] += 1 

total_reprovados = alunos_reprovados['falta'] + alunos_reprovados['nota'] - alunos_reprovados['ambos'] # tanto o total quanto os print's, tiveram o valor diminuido pelo ambos, para que a informação não apareça de forma duplicada

print('De todos os alunos que reprovaram quantos foram por falta e quantos foram por nota, e quantos foram por ambas as causas?\n')

print('Resposta:')
print('+','-'*31,'+')
print(f'| {total_reprovados} Alunos foram reprovados    | \n|                                 |'
'\n| Pelos seguintes motivos:        |\n|                                 |')
print(f'| {alunos_reprovados["falta"] - alunos_reprovados["ambos"]}  Exclusivamente por faltas |')
print(f'| {alunos_reprovados["nota"] - alunos_reprovados["ambos"]}  Exclusivamente por notas  |')
print(f'| {alunos_reprovados["ambos"]}   Por ambos os motivos      |')
print('+','-'*31,'+')