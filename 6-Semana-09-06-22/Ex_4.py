# Construa uma função que desenhe um retângulo usando os caracteres ‘+’ ,
# ‘−’ e ‘| ‘. Esta função deve receber dois parâmetros, linhas e colunas, sendo
# que o valor por omissão é o valor mínimo igual a 1 e o valor máximo é 20. Se
# valores fora da faixa forem informados, eles devem ser modificados para
# valores dentro da faixa

import os

os.system('clear')
from random import randint


linha = int(input('informe a linha: '))
while linha < 1 or linha > 20:
    linha = randint(1, 20)
coluna = int(input('informe a coluna: '))
while coluna < 1 or coluna > 20:
    coluna = randint(1, 20)

def retangulo(a, b):
    if a > b:
        limite = b
        sup_inf = ('-')
        sup_inf = (sup_inf * (a + 4))
        print(sup_inf)
        for i in range(0, b):
            print('|', ('+' * a).ljust(limite), '|')
        print(sup_inf)

    elif b > a:
        limite = a
        sup_inf = ('-')
        sup_inf = (sup_inf * (a + 4))
        print(sup_inf)
        for i in range(0, b):
            print('|', ('+' * a).ljust(limite), '|')
        print(sup_inf)

c = retangulo(linha, coluna)



