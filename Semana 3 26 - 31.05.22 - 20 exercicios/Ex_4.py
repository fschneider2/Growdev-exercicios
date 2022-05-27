# Escreva um algoritmo para ler uma temperatura em graus Fahrenheit,
# calcular e escrever o valor correspondente em graus Celsius (baseado na
# fórmula abaixo): c = F -32
#                 ---  -----     
#                  5     9    

temp_fahrenjeit = float(input('Informe a temperatura, em graus Fahrenhait, que irei converter para Celcius: '))
celcius = (temp_fahrenjeit - 32) / 1.8
print('A temperatura de ',temp_fahrenjeit,'° Fahrenhait, equivale a ',celcius,'° Celcius.')