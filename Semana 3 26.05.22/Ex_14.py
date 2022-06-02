# Faça um algoritmo para ler a temperatura atual e conforme leitura, imprima o
# resultado de acordo com a tabela abaixo.

# Temperatura Resultado
# até 15°       Muito frio
# de 16° à 22°  Frio
# de 23° à 26°  Agradável
# de 27° à 30°  Quente
# 31° ou mais   Muito quente

print('informe a temperatura, que te direi minha opinião sobre o tempo: ')
temp = float(input())

if temp <= 15:
    print('Esta muito frio!!!')

elif temp >= 16 and temp <= 22:
    print('Esta frio!')

elif temp >= 23 and temp <= 26:
    print('Esta Agradável')

elif temp >=27 and temp <= 30:
    print('Esta quente!')

elif temp >= 31:
    print('Esta muito quente!!!')
