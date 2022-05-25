# Conversão de graus Celsius para Fahrenheit – Crie um algoritmo que converta graus 
# Celsius em Fahrenheit. A fórmula é a seguinte:
# 𝐹 =   9 𝐶 + 32
#𝐹 =   9 𝐶 + 32
#        5
# O programa deve solicitar ao usuário que insira uma temperatura em graus Celsius e, 
# em seguida, exiba a temperatura convertida em Fahrenheit. Após construir esse algoritmo, 
# modifique-o para que converta graus Fahrenheit em graus Celsius.
temp_celcius = float(input('Informe a temperatura, em graus Celcius, que irei converter para Fahrenheit: '))
fahrenheit = (1.8 * temp_celcius) + 32
print('A temperatura de ',temp_celcius,'° Celcius, equivale a ',fahrenheit,'° Fahrenheit')
temp_fahrenjeit = float(input('Informe a temperatura, em graus Fahrenhait, que irei converter para Celcius: '))
celcius = (temp_fahrenjeit - 32) / 1.8
print('A temperatura de ',temp_fahrenjeit,'° Fahrenhait, equivale a ',celcius,'° Celcius.')