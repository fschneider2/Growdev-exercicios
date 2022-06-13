# Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.
import os

os.system('clear')

def somar(a, b, c):
    soma = a + b + c
    return soma

calculo = somar(9,2,3)
print(calculo)