# Faça um algoritmo para ler a quantidade adquirida e o preço unitário de um
# produto.
# a) Calcular e escrever o total

# total = quantidade adquirida * preço unitário
# b) Leia o desconto sobre a compra e calcule.

# total a pagar = total - desconto
# i) Sabendo-se que:
# (1) Se quantidade <= 5 o desconto será de 2%.
# (2) Se quantidade > 5 e quantidade <=10 o desconto será de
# 3%.
# (3) Se quantidade > 10 o desconto será de 5%.
quantidade = float(input('Informe a quantidade de itens comprado: '))
valor = float(input('Informe o valor unitario: R$ '))
valor_total = quantidade * valor
print('O valor total é: R$ {}'.format(valor_total))
desconto_1 = valor_total - (quantidade / 100 * 2) 
desconto_2 = valor_total - (quantidade / 100 * 3) 
desconto_3 = valor_total - (quantidade / 100 * 5) 
if quantidade <= 5:
    print('O valor a pagar é R$ {}'.format(desconto_1))
elif quantidade > 5 and quantidade <=10:
    print('O valor a pagar é R$ {}'.format(desconto_2))
elif quantidade > 10:
    print('O valor a pagar é R$ {}'.format(desconto_3))