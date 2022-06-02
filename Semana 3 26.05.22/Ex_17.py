# Faça um programa que pergunte ao usuário se ele quer passar uma
# temperatura de Fahrenheit para Celsius ou de Celsius para Fahrenheit, e
# que, a partir da resposta do usuário, faça a devida conversão.

print('Digite 1 para converter de Celsius para Fahrenheit ou 2 para converter de Fahrenheit para Celsius')

escolha = int(input('Digite 1 ou 2: '))

temperatura =  float(input('Agora informe a temperatura: '))

if escolha == 1:
    fahrenheit = (1.8 * temperatura) + 32
    print('{}° Celcius, equivale a , {}° Fahrenheit'.format(temperatura, fahrenheit))

elif escolha == 2:
    celcius = (temperatura - 32) / 1.8
    print('{}° Fahrenheit  equivale a {}° Celcius,'.format(temperatura, celcius))