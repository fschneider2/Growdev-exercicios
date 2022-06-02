# Escrever um programa que lê um valor N inteiro e positivo e que calcula e
# escreve o valor de E.
# E = 1 + 1 / 1! + 1 / 2! + 1 / 3! + … + 1 / N!

# entrada dados
n = int(input('Informe um numero maior que 0: '))

# laço de repetição para evitar que usuario insira numero negativo, se for inserido um float, codigo quebra.
while not (n > 0):
    n = int(input('Informe um numero maior que 0: '))

# usei o for para criar um laço de repetição, que irá de 1 até o n° anterior a n e armazei isso em x
# dessa forma, ao criar uma variavel e e adicionar a ela 1, teremos a resposta do exercicio. Se n == 3 :
# E = (0 + 1 / 1!) (1! + 1 / 2! (1! é a resposta de 1 + x)) (2! + 1 / 3!) 
for x in range(0, n):
    e = 1 + x
    print(f'E = {x} + 1 / {e}!')