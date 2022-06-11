# Escreva um programa que receba a posição de dois pontos em um espaço 2D, 
# ou seja, cada ponto tem coordenadas x e y, e calcule a distância entre esses dois pontos, 
# exibindo-a na tela..
from math import sqrt
print('Informe as coordenadas do ponto 1 :')
ponto1_x = float(input('X '))
ponto1_y = float(input('Y '))
print('Informe as coordenadas do ponto 2 :')
ponto2_x = float(input('X '))
ponto2_y = float(input('Y 1'))
distancia12 = sqrt((ponto1_x - ponto2_x)**2) + ((ponto1_y - ponto2_y)**2)
print('A distancia entre os pontos 1 e 2 é de: ', distancia12,)