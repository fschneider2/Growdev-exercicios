# Quantos alunos do 3º ano reprovaram? e desses quantos procuraram monitoria?

from funcoes import importar_arquivo

import os

os.system('clear')

dados = importar_arquivo()

alunos_reprovados_mentoria = {'alunos': 0, 'monitoria':0}

for i in dados:
    if i['ano'] == 3:

        if i['faltas'] > 15:
            alunos_reprovados_mentoria['alunos'] += 1 
            if i['monitoria'] == 'True':
                    alunos_reprovados_mentoria['monitoria'] += 1


        elif i['media'] < 7 and i['nota_exame'] <= 5:
                alunos_reprovados_mentoria['alunos'] += 1 
                if i['monitoria'] == 'True':
                    alunos_reprovados_mentoria['monitoria'] += 1


print('Quantos alunos do 3º ano reprovaram? e desses quantos procuraram monitoria? \n')

print('Resposta:')
print('+','-'*31,'+')
print(f'| {alunos_reprovados_mentoria["alunos"]} alunos do 3° ano reprovaram |\n| {alunos_reprovados_mentoria["monitoria"]} destes procuraram monitoria |')        
print('+','-'*31,'+')
