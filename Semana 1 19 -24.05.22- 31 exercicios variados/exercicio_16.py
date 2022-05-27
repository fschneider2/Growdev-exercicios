# Faça um programa que receba o cateto oposto e o cateto adjacente de um triângulo e retorne a 
# hipotenusa do mesmo.
from math import sqrt
cateto_oposto =  float(input('Informe o cateto oposto do triangulo: '))
cateto_adjacente =  float(input('Informe o cateto adjacente do triangulo: '))
calc_lados= (cateto_oposto**2) + (cateto_adjacente**2)
print('A hipotenusa é: ',sqrt(calc_lados))