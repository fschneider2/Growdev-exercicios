# 20) Dado que uma empresa possui valores variáveis de suas ações ao longo do tempo, 
# e que existe sempre uma taxa (que também é variável) a ser paga para realizar transações de compra 
# e venda, escreva um programa que peça a quantidade de ações compradas, o valor da ação naquele
#  período e qual a taxa que foi paga, peça também as mesmas informações em relação a venda de ações.
#  O programa deve exibir:
# a) O valor total gasto na compra de ações
# b) O valor pago em taxa durante a compra
# c) O valor total ganho na venda das ações
# d) O valor pago na venda
# e) O valor de diferença total entre a compra e a venda

quantidade_comprada = int(input('informe a quantidade de ações compradas: '))
valor_pago = float(input('Informe o valor pago por cada ação: R$ '))
taxa = float(input('Informe a taxa paga: R$ '))
valor_pago_total = (quantidade_comprada * valor_pago) + taxa
print('Voce comprou ',quantidade_comprada,'ações | Pagou: R$',valor_pago_total,'| Sendo: R$',valor_pago*quantidade_comprada,'em ações e R$',taxa, 'em taxas')
quantidade_venda = quantidade_comprada
valor_vendido = float(input('Informe o valor recebido por cada ação: R$ '))
taxa_venda = float(input('Informe a taxa paga: R$ '))
valor_recebido_total = (quantidade_venda * valor_vendido) - taxa_venda
lucro = valor_recebido_total - valor_pago_total
print('Voce vendeu: ',quantidade_venda,'| Recebendo: R$',valor_recebido_total,'| Onde pagou: R$',taxa_venda,'de taxa de venda, e lucrou com essa operação: R$',lucro)