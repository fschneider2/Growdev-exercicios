# Escreva um algoritmo que receba a idade do usuário e exiba a mensagem
# “Maior de idade” caso a idade seja maior ou igual de 18 anos e a mensagem
# “Menor de idade” caso a idade seja menor de 18 anos.
idade = int(input('Qual sua idade?: '))
if idade >= 18:
    print('Maior de idade')
else:
    print('Menor de idade')