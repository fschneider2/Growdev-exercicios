# Escreva um programa que receba 3 valores e some as partes decimais de todos eles. 
# Ex: 5.6, 2.3, 8.0, resultado deve ser 0.9.
num_1 = float(input('Informe o primeiro numero: '))
num_2 = float(input('Informe o segundo numero: '))
num_3 = float(input('Informe o terceiro numero: '))
num_1_int = int(num_1)
num_2_int = int(num_2)
num_3_int = int(num_3)
calc = (num_1 + num_2 + num_3) - (num_1_int + num_2_int + num_3_int)
print(round(calc, 1))