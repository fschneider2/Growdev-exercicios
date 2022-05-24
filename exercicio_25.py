# Escreva um programa que receba um número dentro do intervalo de 1 até 9, e exiba a tabuada 
# desse número.
numero_tabuada = int(input('vamos calcular a tabuada, informe um numero de 1 a 9: '))
for inicial in range(0, 11):
    print('{} x {:2} = {}'.format(numero_tabuada, inicial, numero_tabuada * inicial))


