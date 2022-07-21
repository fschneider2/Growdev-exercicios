# Escreva um programa para solicitar ao usuário o raio r de uma esfera, e calcular o volume V da esfera usando uma função, e exibir o resultado. Utilize
# a seguinte fórmula para determinar o volume: v = (4.0 / 3.0) * ℼ * r³

import math
import os

os.system('clear')

def calculo_volume(r):
    v = (4.0 / 3.0) * math.pi * (r**3)
    return v

print('-'*40)
raio = float(input('\nInforme o Raio em metros, que irei lhe apresentar o volume da esfera: '))

volume = calculo_volume(raio)

print(f'\nO volume da esfera é: {round(volume, 2)} metros³')
print('-'*40)