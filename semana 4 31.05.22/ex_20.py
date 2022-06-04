# Escreva um programa que leia um valor inicial A e uma razão R e imprima
# uma sequência em P.G. contendo 10 valores.

a = int(input('Insira o valor inicial para P.A.: '))
r = int(input('Insira a Razão para calculo da P.A.: '))
lista_pa = []

for i in range(1, 11):
    lista_pa.append(a)
    a = a * r
    
print(lista_pa)