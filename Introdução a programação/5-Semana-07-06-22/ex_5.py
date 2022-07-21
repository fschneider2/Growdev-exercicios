# Construa um programa que permita a um usuário informar uma série de números, até que um número negativo seja fornecido. Ao final, imprima o
# somatório desses números, a média, o valor máximo e o mínimo. Desconsidere o último número (negativo) informado pelo usuário

import os
from statistics import mean

os.system('clear')

continuar = True

serie = []

while continuar == True:
    numero = float(input('Digite um número, para encerrar, digite um número menor que 0: '))
    serie.append(numero)

    if numero < 0:
        continuar = False   

del serie [-1]

print(f'A soma dos itens digitados é: {sum(serie)}')
print(f'A Média dos itens digitados é: {mean(serie)}')
print(f'O valor maximo digitado foi: {max(serie)}')
print(f'O valor minimo digitado foi: {min(serie)}')
