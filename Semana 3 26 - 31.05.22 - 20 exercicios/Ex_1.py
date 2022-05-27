# Escreva um algoritmo que receba dois números, exiba as opções:
# a) 1 - adição
# b) 2 - subtração
# Então peça ao usuário para escolher uma das opções. Caso escolha a opção
# 1 o algoritmo deve realizar a soma dos dois números lidos e exibir. Caso
# escolha a opção 2 o algoritmo deve realizar a subtração dos dois números
# lidos e exibir.

num_1 = float(input('Informe o primeiro numero: '))
num_2 = float(input('Informe o segundo numero: '))
adicao = num_1 + num_2
subtracao = num_1 - num_2
ad_sub = float(input('Informe 1 para adição e 2 para subtração: '))
while ad_sub != 1 and ad_sub != 2:
    ad_sub = float(input('Informe 1 para adição e 2 para subtração: '))
if ad_sub == 1:
    print('A soma de {} + {} = {}'.format(num_1, num_2, adicao))
else:
    print('A subtração de {} - {} = {}'.format(num_1, num_2, subtracao))