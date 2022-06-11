# Uma receita de biscoitos exige os seguintes ingredientes para produzir 48 unidades:
# a) 1,5 xícaras de açúcar
# b) 1 xícara de manteiga
# c) 2,75 xícaras de farinha
# Crie um algoritmo que pergunte ao usuário quantos biscoitos ele deseja fazer e calcule a 
# quantidade correspondente dos ingredientes.
un_acucar = 1.5 / 48
un_manteiga = 1 / 48
un_farinha = 2.75 / 48
quantidade_solicitada = float(input('Informe a quantidade de biscoitos que deseja fazer: '))
calc_acucar = un_acucar * quantidade_solicitada
calc_manteiga = un_manteiga * quantidade_solicitada
calc_farinha = un_farinha * quantidade_solicitada
print('Para fabricar',quantidade_solicitada,'biscoitos, você ira precisar de:',round(calc_acucar, 2),'xicaras de açucar. |',round(calc_manteiga, 2),'xicaras de manteiga. | \ne',round(calc_farinha, 2),'xicaras de farinha.')
