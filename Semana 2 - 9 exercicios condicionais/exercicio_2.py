# Faça um algoritmo que receba um valor negativo e retorne o seu valor
# absoluto (ex: recebe -5 e retorna 5).

print('Informe um numero:')
numero = float(input())

numero_absoluto = numero
if numero < 0:
    numero_absoluto = numero * -1
        
print('o absoluto é: {}'.format(numero_absoluto))
