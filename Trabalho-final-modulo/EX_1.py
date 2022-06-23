# Quantos alunos estudam em cada escola, e qual a escola com mais alunos?

from funcoes import importar_arquivo
import os

os.system('clear')

dados = importar_arquivo()

escolas = []
quantidade_alunos_por_escola = []

for i in dados:
    if i['escola'] not in escolas: # se a escola ainda não estiver na lista escolas ele ira adiciona-la
        quantidade_alunos_por_escola.append([1, i['escola']])
        escolas.append(i['escola'])

    else:
        for j in quantidade_alunos_por_escola: # caso já esteja, irá somar 1 ao contador
            if j[1] == i['escola']:  # perceba que a posição de meu contador é a [0], isso, para que possa trabalhar com a função max, sem precisar lidar com meu dados novamente.
                j[0] += 1 

escola_com_mais_alunos = max(quantidade_alunos_por_escola) # utilizado para localizar a escola com mais alunos

print('Quantos alunos estudam em cada escola? \n')


print('Resposta:')
print('+','='*45,'+')

for i in quantidade_alunos_por_escola: # laço utilizado para apresentar as escolas e quantidade de alunos
    print(f'# Escola {i[1]}, Total de alunos: {i[0]}')
    
print('+','='*45,'+')
print('\nE qual a escola com mais alunos?\n')

print('Resposta:')
print('+','='*65,'+')
print(f'# A escola com mais alunos é {escola_com_mais_alunos[1]}, com {escola_com_mais_alunos[0]} alunos.')
print('+','='*65,'+')