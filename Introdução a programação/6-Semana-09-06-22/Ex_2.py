# Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’, se seu argumento for positivo, 
# e ‘N’, se seu argumento for zero ou negativo.
import os

os.system('clear')

def positivo_negativo(a):
    if a > 0:
        return 'P'
    else:
        return 'N'

p_n = positivo_negativo(5)