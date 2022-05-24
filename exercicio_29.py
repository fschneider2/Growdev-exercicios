# Crie um algoritmo que calcule e exiba a conversão de uma determinada quantidade em 
# reais em moedas de R$1.00, R$0.50, R$0.25, R$0.10, R$0.05 e R$0.01. Por exemplo, R$3.78 
# resulta em três moedas de um real, uma de cinquenta centavos, duas de dez centavos, uma de 
# 5 centavos e três de um centavo.
valor = float(input('Informe o valor: R$'))
moeda_1 = valor / 1
resto_1 = valor % 1
moeda_050 = resto_1 / 50
resto_050 = moeda_050 % 50
moeda_025 = resto_050 / 25
resto_025 = moeda_025 % 25
moeda_010 = resto_025 / 10
resto_010 = moeda_010 % 10
moeda_005 = resto_010 / 5
resto_005 = moeda_005 % 5
moeda_001 = resto_005 / 1
resto_001 = moeda_001 % 1
if(moeda_1 > 0):
    print('Moedas de R$ 1,00 = ',round(moeda_1, 0))
