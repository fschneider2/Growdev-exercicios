# Um cliente de uma loja está comprando cinco produtos. Crie um programa que solicite 
# o preço de cada um desses produtos e, em seguida, exiba o subtotal da venda, o valor 
# do imposto e o valor total (subtotal da venda mais o valor do imposto). Suponha que a alíquota 
# do imposto seja de 6% sobre o subtotal da venda.
produto_1 = float(input('informa o valor do produto 1: R$ '))
produto_2 = float(input('informa o valor do produto 2: R$ '))
produto_3 = float(input('informa o valor do produto 3: R$ '))
produto_4 = float(input('informa o valor do produto 4: R$ '))
produto_5 = float(input('informa o valor do produto 5: R$ '))
valor_produtos = produto_1 + produto_2 + produto_3 + produto_4 + produto_5
valor_imposto = (valor_produtos / 100) * 6
valor_total = valor_produtos + valor_imposto
print('O valor dos produtos é: R$', valor_produtos)
print('O valor do imposto é: R$', valor_imposto)
print('O valor total a ser pago é de: R$', valor_total)