# Escreva um algoritmo que leia 3 valores e exiba qual o maior valor entre eles.
num_1 = float(input('Informe o primeiro valor: '))
num_2 = float(input('Informe o segundo valor: '))
num_3 = float(input('Informe o terceiro valor: '))
if num_1 > num_2 and num_1 > num_3:
    print('O primeiro valor é o maior: {}'.format(num_1))
elif num_2 > num_1 and num_2 > num_3:
    print('O segundo valor é o maior: {}'.format(num_2))
elif num_3 > num_1 and num_3 > num_2:
    print('O terceiro valor é o maior: {}'.format(num_3))