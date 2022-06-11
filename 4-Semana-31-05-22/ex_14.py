# Desenvolver um programa que efetue a soma de todos os números ímpares
# que se encontram no conjunto dos números de 1 até 500.

varia = 500
lista_impares = []

for i in range(1, varia, 2):
    lista_impares.append(i)

print(f'A soma dos impares é: {sum(lista_impares)}')
