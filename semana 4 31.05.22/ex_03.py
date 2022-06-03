# Escrever um programa que lê um valor N inteiro e positivo e que calcula e
# escreve o valor de E.
# E = 1 + 1 / 1! + 1 / 2! + 1 / 3! + … + 1 / N!

# entrada dados
n = int(input('Informe um numero maior que 0: '))

somatorio = 1




for x in range(1, n + 1):
    fatorial = 1
    for valor in range(x, 1, -1):
        fatorial = fatorial * valor
    somatorio = somatorio +1/ fatorial

print(f'E = {somatorio}')