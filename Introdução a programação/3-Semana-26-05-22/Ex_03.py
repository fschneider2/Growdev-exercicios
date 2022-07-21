# O custo de um carro novo ao consumidor é a soma do custo de fábrica com a
# porcentagem do distribuidor e dos impostos (aplicados ao custo de fábrica).
# Supondo que o percentual do distribuidor seja de 28% e os impostos de 45%,
# escrever um algoritmo para ler o custo de fábrica de um carro, calcular e
# escrever o custo final ao consumidor.
custo_fabrica = float(input('Informe o custo de fabrica:R$ '))
calc_distrib = custo_fabrica / 100 * 28
calc_imposto = custo_fabrica / 100 * 45
preco_final = custo_fabrica + calc_distrib + calc_imposto
print('O carro irá custar: R$ {}, ao consumidor final'.format(preco_final))