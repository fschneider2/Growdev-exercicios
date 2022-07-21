# Faça um Programa que leia um número inteiro menor que 1000 e imprima a
# quantidade de centenas, dezenas e unidades do mesmo. Exemplos:
# 326 = 3 centenas, 2 dezenas e 6 unidades
# 12 = 1 dezena e 2 unidades

num_inteiro = int(input('Informe o numero inteiro menor que 1000: '))
while num_inteiro >= 1000:
    num_inteiro = int(input('Informe o numero inteiro menor que 1000: '))

uni = num_inteiro // 1 % 10
dez = num_inteiro // 10 % 10
cent = num_inteiro // 100 % 10
print('{} possui: {} Centenas, {} Dezenas e, {} Unidades'.format((num_inteiro),(cent),(dez),(uni)))