# Desenvolver um programa que leia um número não determinado de valores
# e calcule e escreva a média aritmética dos valores lidos, a quantidade de
# valores positivos, a quantidade de valores negativos e o percentual de
# valores negativos e positivos.
from statistics import mean
import os

c_n = 0
c_p = 0
lista_vazia = []
continuar = False

while continuar == False:
    numero = float(input('Informe um número: '))
    lista_vazia.append(numero)
    if numero <= 0:
        c_n += 1
    else:
        c_p += 1

    info = int(
        input('Para continuar digite 1, para parar digite qualquer digito: '))

    if info == 1:
        pass
    else:
        continuar = True

    os.system('clear')

media = mean(lista_vazia)
total = c_n + c_p
percental_n = (c_n * 100) / total
percental_p = (c_p * 100) / total

print(f'A média aritmética dos numeros digitados é: {media}')
print(f'{c_p} São positivos')
print(f'{c_n} São negativos')
print(f'{percental_n} % São negativos')
print(f'{percental_p} % São positivos')

