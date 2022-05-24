# Faça um programa que receba um valor no intervalo entre 0 e 1000, 
# e converta para o valor correspondente ao intervalo -1 e 1.
valor_0_1000 = int(input('Informe um valor entre 1 e 1000, que irei converter para o valor correspondente ao intervalo -1 e 1: '))
converta = valor_0_1000 / valor_0_1000 - 1
print('O resultado da conversão é:',converta)