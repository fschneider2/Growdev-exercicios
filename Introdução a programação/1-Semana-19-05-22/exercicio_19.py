# Faça um programa que receba os coeficientes a, b e c da equação a seguir, e encontre as raízes
#  por meio da fórmula de bhaskara.
#   2
# 𝑎𝑥 + 𝑏𝑥 + 𝑐
from math import sqrt
a = float(input('Informe o valor de a: '))
b = float(input('Informe o valor de b: '))
c = float(input('Informe o valor de c: '))

# calculei o delta, para facilitar o calculo dos x, peguei essa dica com Francisco Chaves, no google.
delta = (b **2) -4 * a * c
if a == 0:
    print('O Valor de a deve ser diferente de 0')
elif delta < 0:
    print('Sem raizes reais')
else:
    x1 = (-b + sqrt(delta)) / (2 * a)
    x2 = (-b - sqrt(delta)) / (2 * a)
    # peguei essa variação na internet, sem usar o sqrt x1 = (-b + delta ** (1/2)) / (2 * a)
    # peguei essa variação na internet, sem usar o sqrt x2 = (-b - delta ** (1/2)) / (2 * a)
    print('X1 = ',x1, ', X2 = ',x2)