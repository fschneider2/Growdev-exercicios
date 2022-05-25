# Crie um algoritmo para uma empresa de transportes que, a partir do peso de
# uma encomenda fornecida pelo usuário, calcule o preço da remessa
# conforme a seguinte tabela:

# Peso da encomenda                              Valor
# 500 gramas ou menos                            R$ 1,10
# Mais de 500 gramas, mas não maisque 2 quilos   R$ 2,20
# Mais de 2 quilos, mas não mais de 10 quilos    R$ 3,70
# Mais de 10 quilos                              R$ 5,00 mais R$ 3,80/kg pelo peso que ultrapassar 10 Kg

peso_encomenda = float(input('informe quantos kg pesa a encomenda, se gramas, utiliza 0., 0.500, por exemplo: '))
peso_gramas = peso_encomenda * 1000
if peso_gramas <= 500:
    print('O valor da encomenda é R$ 1.10')
elif peso_gramas > 500 and peso_gramas <= 2000 :
    print('O valor da encomenda é R$ 2.20')
elif peso_gramas > 2000 and peso_gramas <= 10000:
    print('O valor da encomenda é R$ 3.70')
elif peso_gramas > 10000:
    print('O valor da encomenda é R$ 8.80')
