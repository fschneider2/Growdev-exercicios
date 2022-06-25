# Qual dos anos (1º, 2º ou 3º) mais procura a monitoria?. Crie um gráfico para mostrar esses dados.

from matplotlib import pyplot

from funcoes import importar_arquivo

import os

os.system('clear')

dados = importar_arquivo()

alunos_monitoria = {'alunos_1': 0, 'alunos_2': 0, 'alunos_3': 0}

def monitoria(a, b):
    for i in dados:
        if i['ano'] == a and i['monitoria'] == 'True':
            alunos_monitoria[b] += 1 


monitoria(1, 'alunos_1')
monitoria(2, 'alunos_2')
monitoria(3, 'alunos_3')

primeiro_ano = alunos_monitoria['alunos_1']
segundo_ano = alunos_monitoria['alunos_2']
terceiro_ano = alunos_monitoria['alunos_3']

print(primeiro_ano, segundo_ano, terceiro_ano)

print('Qual dos anos (1º, 2º ou 3º) mais procura a monitoria? \n')

print('Resposta: ')

print('+','-'*55,'+')
if primeiro_ano > segundo_ano and primeiro_ano > terceiro_ano:
    print('| A monitoria é mais procurada entre os alunos do 1° ano |')

elif primeiro_ano < segundo_ano and segundo_ano > terceiro_ano:
    print('|  A monitoria é mais procurada entre os alunos do 2° ano |')

else:
    print('|  A monitoria é mais procurada entre os alunos do 3° ano |')
print('+','-'*55,'+')

x = ['1°', '2°', '3°']
y = [primeiro_ano, segundo_ano, terceiro_ano]   
    
fig, ax = pyplot.subplots()
ax.bar(x, y)
pyplot.title(f'Qual dos anos (1º, 2º ou 3º) mais procura a monitoria?')
pyplot.show()