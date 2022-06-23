# Quantos alunos do 3º ano reprovaram? e desses quantos procuraram monitoria?

from funcoes import importar_arquivo

import os

os.system('clear')

dados = importar_arquivo()

alunos_reprovados_mentoria = {'alunos': 0, 'monitoria':0}

for i in dados:

    if i['ano'] == 3: # o laço inicia analisando se os alunos são do 3° ano

        if i['faltas'] > 15: # caso sim, vamos analisar primeiro quem foi reprovado por faltas, dessa forma já elimino conto estes
            alunos_reprovados_mentoria['alunos'] += 1 
            if i['monitoria'] == 'True': # e dentro de cada laço de reptição, ele já verifica e conta os alunos que procuraram a monitoria
                    alunos_reprovados_mentoria['monitoria'] += 1


        elif i['media'] < 7 and i['nota_exame'] <= 5: # após verificado e eliminado quem foi reprovado por faltas, ele verifica quem foi reprovado por média, a média já foi incluida no dicionario principal, dentro do arquivo dicionario_e_int
                alunos_reprovados_mentoria['alunos'] += 1 
                if i['monitoria'] == 'True':
                    alunos_reprovados_mentoria['monitoria'] += 1


print('Quantos alunos do 3º ano reprovaram? e desses quantos procuraram monitoria? \n')

print('Resposta:')
print('+','-'*31,'+')
print(f'| {alunos_reprovados_mentoria["alunos"]} alunos do 3° ano reprovaram |\n| {alunos_reprovados_mentoria["monitoria"]} destes procuraram monitoria |')        
print('+','-'*31,'+')
