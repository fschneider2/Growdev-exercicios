# Escreva um algoritmo que receba um número e escreva “Par” caso esse
# número seja par e escreva “Impar” caso esse número seja impar.
numero = int(input('Informe um numero: '))
formula = numero % 2 
if formula == 1:
    print('Impar')
else:
    print('Par')