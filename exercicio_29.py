# Crie um algoritmo que calcule e exiba a conversão de uma determinada quantidade em 
# reais em moedas de R$1.00, R$0.50, R$0.25, R$0.10, R$0.05 e R$0.01. Por exemplo, R$3.78 
# resulta em três moedas de um real, uma de cinquenta centavos, duas de dez centavos, uma de 
# 5 centavos e três de um centavo.
valor = float(input('Informe o valor: R$'))
moeda_1 = valor / 100
resto_1 = valor % 100
moeda_050 = resto_1 / 50
resto_050 = resto_1 % 50
moeda_025 = resto_050 / 25
resto_025 = resto_050 % 25
moeda_010 = resto_025 / 10
resto_010 = resto_025 % 10
moeda_005 = resto_010 / 5
resto_005 = resto_010 % 5
moeda_001 = resto_005 / 1
resto_001 = resto_005 % 1
if(moeda_1 > 0):
    print('Moedas de R$ 1,00 = ',moeda_1)
if(moeda_050 > 0):
    print('Moedas de R$ 0,50 = ',moeda_050)
if(moeda_025 > 0):
    print('Moedas de R$ 0,25 = ',moeda_025)
if(moeda_010 > 0):
    print('Moedas de R$ 0,10 = ',moeda_010)
if(moeda_005 > 0):
    print('Moedas de R$ 0,05 = ',moeda_005)
if(moeda_001 > 0):
    print('Moedas de R$ 0,01 = ',moeda_001)

