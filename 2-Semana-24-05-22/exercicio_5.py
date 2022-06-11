# Escreva um algoritmo que leia três números fornecidos pelo usuário e mostre
# se a soma de dois deles resulta no terceiro.
num_1 = float(input('Informe o 1° numero: '))
num_2 = float(input('Informe o 2° numero: '))
num_3 = float(input('Informe o 3° numero: '))

if num_1 + num_2 == num_3:
    print('A soma do 1° e do 2° é = 3°')
elif num_1 + num_3 == num_2:
    print('A soma do 1° e do 3° é = 2°')
elif num_2 + num_3 == num_1:
    print('A soma do 2° e do 3° é = 1°')
else:
    print('A soma de 2 digitos informados, não resulta num terceiro')