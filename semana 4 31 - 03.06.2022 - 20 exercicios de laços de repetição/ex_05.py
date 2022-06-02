# Chico tem 1,50 metro e cresce 2 centímetros por ano, enquanto Zé tem 1,10
# metro e cresce 3 centímetros por ano. Construa um programa que calcule e
# imprima quantos anos serão necessários para que Zé seja maior que Chico.

contador = 0
chico = 150
ze = 110
while ze <= chico:
    ze += 3
    chico += 2
    contador += 1
print(f'Zé vai demorar {contador} anos para ser maior que Chico')