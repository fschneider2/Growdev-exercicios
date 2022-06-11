# Escreva um algoritmo que receba 3 números, faça a soma dos dois primeiros
# e verifique se o resultado da soma é maior que o terceiro número lido.
num_1 = float(input('Informe o 1° numero: '))
num_2 = float(input('Informe o 2° numero: '))
num_3 = float(input('Informe o 3° numero: '))

if num_1 + num_2 > num_3:
    print('A soma do 1° e do 2° é maior que o 3°')
# elif num_1 + num_3 > num_2:
#     print('A soma do 1° e do 3° é > 2°')
# elif num_2 + num_3 > num_1:
#     print('A soma do 2° e do 3° é > 1°')
else:
    print('A soma dos 2 primeiros digitos informados, não é maior que o terceiro')