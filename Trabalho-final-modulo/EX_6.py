# As reprovações são maiores entre os alunos do 1º, 2º ou 3º ano?. Crie um gráfico para mostrar isso.

from matplotlib import pyplot

from funcoes import importar_arquivo

import os

os.system('clear')

dados = importar_arquivo()

# resolução do problema 

alunos_reprovados = {'alunos_1': 0, 'alunos_2': 0, 'alunos_3': 0}

def reprovados(arquivo, ano, variavel, chave): # criada função para que se obtenha a quantidade de reprovados por ano
    for i in arquivo:
        if i['ano'] == ano:
            if i['faltas'] > 15 or i['faltas'] <= 15 and i['media'] < 7 and i['nota_exame'] < 5:
                variavel[chave] += 1 

reprovados(dados, 1, alunos_reprovados, 'alunos_1') 
reprovados(dados, 2, alunos_reprovados, 'alunos_2')
reprovados(dados, 3, alunos_reprovados, 'alunos_3')

# puxei as informações dessa forma para facilitar a comparação entre os anos 
primeiro_ano = alunos_reprovados['alunos_1']
segundo_ano = alunos_reprovados['alunos_2']
terceiro_ano = alunos_reprovados['alunos_3']

print(primeiro_ano, segundo_ano, terceiro_ano)

print('As reprovações são maiores entre os alunos do 1º, 2º ou 3º ano?\n')

print('Resposta: ')
print('+','-'*52,'+')
if primeiro_ano > segundo_ano and primeiro_ano > terceiro_ano:
    print('| As reprovações são maiores entre os alunos do 1° ano |')

elif primeiro_ano < segundo_ano and segundo_ano > terceiro_ano:
    print('| As reprovações são maiores entre os alunos do 2° ano |')

else:
    print('| As reprovações são maiores entre os alunos do 3° ano |')
print('+','-'*52,'+')

# Plotagem do gráfico 

x = ['1°', '2°', '3°']
y = [primeiro_ano, segundo_ano, terceiro_ano]   
    
fig, ax = pyplot.subplots()
ax.bar(x, y)
pyplot.title(f'As reprovações são maiores entre os alunos do 1º, 2º ou 3º ano?')
pyplot.show()