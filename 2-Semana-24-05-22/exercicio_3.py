# Um brechó revende produtos usados, e fixa o preço de venda de cada
# produto conforme o valor de sua aquisição. Se o preço de aquisição de um
# produto é menor do de R$ 50.00, ele deve ser vendido por um preço 45%
# maior; caso contrário, o lucro será de 30%. Sabendo disso, construa um
# algoritmo que leia o valor de aquisição de um produto e mostre o seu valor de
# venda.

valor_de_compra =  float(input('Informe o valor de compra: R$ '))

valor_venda_1 = valor_de_compra / 0.70 
valor_venda_2 = valor_de_compra / 0.55

if valor_de_compra < 50:
    print('O valor de venda é: R$ {}'.format(valor_venda_2))
else:
    print('O valor de venda é: R$ {}'.format(valor_venda_1))