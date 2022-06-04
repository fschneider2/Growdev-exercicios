# Escreva um programa que imprima na tela a tabuada de um número fornecido pelo usuário, de 1 a 10.

numero_tabuada = int(input('vamos calcular a tabuada, informe um numero de 1 a 9: '))

for inicial in range(0, 11):

    print('{} x {:2} = {}'.format(numero_tabuada, inicial, numero_tabuada * inicial))



