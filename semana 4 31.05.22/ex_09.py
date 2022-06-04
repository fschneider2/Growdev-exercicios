# Escreva um programa que receba o nome de 10 pessoas e para cada
# pessoa, o lugar para o qual ela já viajou. Sendo que existem 3 possibilidades:
# a) Rio de Janeiro
# b) Bahia
# c) Minas Gerais
# Após, informar qual foi o destino mais visitado e qual o menos visitado

rJ = 0
bHia = 0
mG = 0
contador = 1
mais_visitado = 0
menos_visitado = 0
print('--'*13)

while contador <= 10:
    visita = int(input('Para onde você já viajou? Informe 1 para Rio de Janeiro, 2 para Bahia e 3 para Minas Gerais: '))
    while visita != 1 and visita != 2 and visita != 3:
        visita = int(input('Para onde você já viajou? Informe 1 para Rio de Janeiro, 2 para Bahia e 3 para Minas Gerais: '))
    if visita == 1:
        rJ += 1
    elif visita == 2:
        bHia += 1
    elif visita == 3:
        mG += 1
    contador += 1

print(rJ)
print(bHia)
print(mG)

if rJ > bHia and rJ > mG:
    mais_visitado = 'Rio de Janeiro'
elif bHia > rJ and bHia > mG:
    mais_visitado = 'Bahia'
elif mG > rJ and  mG > bHia:
    mais_visitado = 'Minas Gerais'

if rJ < bHia and rj < mG:
    menos_visitado = 'Rio de Janeiro'    
elif bHia < rJ and bHia < mG:
    menos_visitado = 'Bahia'
elif mG < rJ and  mG < bHia:
    menos_visitado = 'Minas Gerais' 

print(f'O estado mais visitado foi: {mais_visitado} e o menos visitado foi:  {menos_visitado}')