# Escrever um programa que lê 5 valores para a, um de cada vez, e conta
# quantos destes valores são negativos, escrevendo esta informação.

contador = 0
for a in range(5):
    a = int(input('Digite um numero: '))
    if a < 0:
        contador += 1
print(f'{contador} dos numeros digitados são negativos')