# Quadrado mágico. Um quadrado mágico é aquele dividido em linhas e colunas, com um número em cada posição e no qual a soma das linhas,
# colunas e diagonais é a mesma. 

# Por exemplo, veja um quadrado mágico de lado 3, com números de 1 a 9:
# 8  3  4
# 1  5  9 
# 6  7  2

# Elabore uma função que identifica e mostra na tela todos os quadrados mágicos com as características acima. Dica: produza todas as combinações
# possíveis e verifique a soma quando completar cada quadrado.

import os
os.system('clear')
import random

lista = [[0,0,0],[0,0,0],[0,0,0]]
numeros = [1,2,3,4,5,6,7,8,9]
quadrado_magico = []
lista2 = []
contador = 0
quantos_quadrados = 1

while numeros != []:
    for i in range(3):
        for j in range(3):
            z = random.shuffle(numeros)
            lista[i][j] = z 
            # numeros.remove(z)
    quantos_quadrados += 1
    
a1 = lista[0][0]
a2 = lista[0][1]
a3 = lista[0][2]
b1 = lista[1][0]
b2 = lista[1][1]
b3 = lista[1][2]
c1 = lista[2][0]
c2 = lista[2][1]
c3 = lista[2][2]

# info_quadrado_magico = b2 == 5 and a1 + a2 + a3 == 15 and b1 + b2 + b3 == 15 and c1 + c2 + c3 == 1 and a1 + b1 + c1 == 15 and a2 + b2 + c2 == 15 and a3 + b3 + c3 == 15 and a1 + b2 + c3 == 15 and a3 + b2 + c1 == 15 

while quantos_quadrados < 40000:

    a1 = lista[0][0]
    a2 = lista[0][1]
    a3 = lista[0][2]
    b1 = lista[1][0]
    b2 = lista[1][1]
    b3 = lista[1][2]
    c1 = lista[2][0]
    c2 = lista[2][1]
    c3 = lista[2][2]

    if b2 == 5 and a1 + a2 + a3 == 15 and b1 + b2 + b3 == 15 and c1 + c2 + c3 == 1 and a1 + b1 + c1 == 15 and a2 + b2 + c2 == 15 and a3 + b3 + c3 == 15 and a1 + b2 + c3 == 15 and a3 + b2 + c1 == 15:
        quadrado_magico.append(lista)
        contador += 1

    else:
        numeros = [1,2,3,4,5,6,7,8,9]
        for i in range(3):
            for j in range(3):
                z = random.shuffle(numeros)
                lista[i][j] = z 
                # numeros.remove(z)
        lista2.append(lista)

    quantos_quadrados += 1
    print(lista)
    print(quadrado_magico)
    print(quantos_quadrados)

