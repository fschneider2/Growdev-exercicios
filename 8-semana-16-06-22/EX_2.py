# Crie uma classe que modele um retângulo:

# a)Atributos:LadoA,LadoB(ou ComprimentoeLargura,ou Base e Altura, a escolher)

# b)Métodos:
# i)Mudar valor dos lados
# ii)Retornar valor dos lados
# iii)Calcular Área
# iv)Calcular Perímetro;

# c)Crie um programa que utilize esta classe
# Ele deve pedir ao usuário que informe as medidas de um local .
# Depois,deve-secriar um objeto com as medidas e calcular a quantidade(em m²)depisos(1x1m²)e de rodapés necessários para o local

from Class import Retangulo

base = int(input('Informe a base '))
altura = int(input('Informe a altura '))

retangulo = Retangulo(base, altura)

pisos = retangulo.calculo_area()

rodapes = retangulo.perimetro()

print(f'Pisos de 1 x 1 m²: {pisos}')
print(f'Rodapes m: {rodapes}')

