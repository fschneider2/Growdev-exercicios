# Faça um programa que peça o nome e as duas notas de 5 alunos, calcule a média das notas e armazene nome e média cada uma em uma lista, ao final
# imprima o nome e o número de alunos com média maior ou igual a 7.0

import os

os.system('clear')

mediaNotas = []
nomes = []
mediaNotas_a = []
nomes_a = []


for i in range(5):
    nome = input('Informe seu nome: ')
    nomes.append(nome)

    nota1 = float(input('Informe sua primeira nota: '))
    nota2 = float(input('Informe sua segunda nota: '))

    media = (nota1 + nota2) / 2
    mediaNotas.append(media)

    if media >= 7:
        nomes_a.append(nome)
        mediaNotas_a.append(media)

print(f'Os alunos aprovados foram: {nomes}, que obtiveram as seguintes médias: {mediaNotas}')






