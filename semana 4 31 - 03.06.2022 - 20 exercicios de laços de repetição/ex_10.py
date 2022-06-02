# Escreva um programa que recebe 10 valores e imprima o somatório dos
# elementos.

contador = 1
lista_numeros = []
# igual exercicio 7, com uma saída diferente..
while contador <= 10:

    numero = int(input('Digite 10 valores, no fim vou lhe informar o maior e o menor: '))
    lista_numeros.append(numero)
    contador += 1

print(f'A soma de todos os numeros infomrados é :{sum(lista_numeros)}')