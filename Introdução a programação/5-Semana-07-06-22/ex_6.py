# Crie um programa que leia continuamente a altura e o sexo de uma lista de pessoas salvando todas as informações em listas, até que uma altura
# negativa seja fornecida. Ao final, sabendo que a média de altura para as mulheres brasileiras é de 1.60m e a dos homens brasileiros é de 1.73m,

# escreva as seguintes informações:
# a) quantas mulheres da lista estão acima da média nacional de altura para mulheres, e quantas estão abaixo;

# b) quantos homens da lista estão acima da média nacional de altura para homens, e quantos estão abaixo.

import os
os.system('clear')


alturaF = []
alturaM = []
baixosM = 0
baixosF = 0

positivo = True

while positivo == True:
    sexo = input('Informe seu sexo: Insira M para masculino e F para feminino: ')
    altura = float(input('Informe sua altura: '))

    if sexo == 'M' or sexo == 'm' and altura > 0:
        alturaM.append(altura)
        if altura < 1.73:
            baixosM += 1

    elif sexo == 'F' or sexo == 'f' and altura > 0:
        alturaF.append(altura)
        if altura < 1.6:
            baixosF += 1

    if altura < 0:
        positivo = False

acimaF = len(alturaF) - baixosF
acimaM = len(alturaM) - baixosM

print(f'{acimaF} Mulheres da lista estão na média ou a cima da média nacional.\n')
print(f'{baixosF} Mulheres da lista estão abaixo da média nacional.\n')
print(f'{acimaM} Homens da lista estão na média ou a cima da média nacional.\n')
print(f'{baixosM} Homens da lista estão abaixo da média nacional.\n')

    