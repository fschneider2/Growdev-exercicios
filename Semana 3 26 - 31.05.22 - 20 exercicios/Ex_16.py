# Construa um algoritmo que, a partir do valor do comprimento dos três lados
# de um triângulo, classifique-o em equilátero, isósceles ou escaleno. Lembre,
# um triângulo é equilátero quando o comprimento de todos os seus lados for
# igual, é isósceles quando apenas um dos lados tiver comprimento diferente e
# é escaleno quando todos os lados tiverem comprimentos diferentes dos
# demais lados.
print('Vou te ajudar a descobrir com que te tipo de triagulo irá trabalhar, se equilátero, isósceles ou escaleno.')

lado_1 = float(input('Informe a medida do lado 1: '))
lado_2 = float(input('Informe a medida do lado 2: '))
lado_3 = float(input('Informe a medida do lado 3: '))

if lado_1 == lado_2 and lado_2 == lado_3:
    print('Seu triangulo possui todos os lados iguais, é um triangulo equilátero.')

elif lado_1 == lado_2 or lado_1 == lado_3 or lado_2 == lado_3:
    print('Seu triangulo possui dois lados iguais e o somente 1 diferente, é um triangulo isósceles.')

elif lado_1 != lado_2 and lado_1 != lado_3 and lado_2 != lado_3:
    print('Seu triangulo possui três lados diferentes, é um triangulo escaleno.')