# # Uma empresa vende um produto a R$5,40 a unidade. Sabendo-se que existe um desconto 
# # acumulado de 0,5% do valor total da compra a cada centena comprada deste produto. 
# # Escreva um algoritmo que receba a quantidade comprada desse produto e informe.
# # a) O valor total da compra (sem o desconto)
# # b) A quantidade de centenas compradas desse produto
# # c) O desconto em R$.
# # d) O valor total da compra (com desconto)

quantidade_comprada = int(input('Informe a quantidade comprada: '))

un = 5.40

total = quantidade_comprada * un

cent = quantidade_comprada // 100 % 10

valor_centena = un * 100

desc_cent = valor_centena * 0.5 / 100

desc = cent * desc_cent             

total_pagar = total - desc

print('O valor total da compra é: R$',round(total, 2))

print('Você comprou',cent, 'centenas deste produto')

print('Por isso, você tem um desconto de: R$',desc)

print('Com valor total a pagar de: R$',round(total_pagar, 2))

