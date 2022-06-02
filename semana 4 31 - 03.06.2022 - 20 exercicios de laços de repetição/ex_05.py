# Chico tem 1,50 metro e cresce 2 centímetros por ano, enquanto Zé tem 1,10
# metro e cresce 3 centímetros por ano. Construa um programa que calcule e
# imprima quantos anos serão necessários para que Zé seja maior que Chico.

# criado o contador, as variaveis chico e ze, e atribui a eles a medida em cm, poderia ter convertido,
#  usando um imput para receber as medidas em metros e depois converter em cm * 100
contador = 0
chico = 150
ze = 110
# enquanto o for menor ou igual ao chico, ele vai add mais um ao contador, o contador é o numero de anos 
while ze <= chico:
    ze += 3
    chico += 2
    contador += 1
# saida solicitada.
print(f'Zé vai demorar {contador} anos para ser maior que Chico')