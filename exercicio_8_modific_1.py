# A padaria do Paulo vende pão francês a R$0.75, pão doce a R$0.85 
# e quindim a R$1.50. Crie um algoritmo que pergunte quantas unidades de cada produto 
# foram vendidas pelo Paulo num dia e calcule o total faturado.

# Modificação 1 – Modifique o algoritmo para que, ao invés de considerar o preço dos produtos 
# como fixos, o usuário possa informar o preço deles.
print('Olá Paulo, vamos calcular o total faturado pela sua padaria no dia de hoje,informe a baixo a quantidade de cada item vendido e após o valor.')
pao_frances = int(input('Pão Frances: '))
pao_doce = int(input('Pão Doce: '))
quindin = int(input('Quindin: '))
valor_pao_frances = float(input('Valo do pão frances: '))
valor_pao_doce = float(input('Valo do pão doce: '))
valor_quindin = float(input('Valo do quindin: '))
total_faturado = (pao_frances * valor_pao_frances) + (pao_doce * valor_pao_doce) + (quindin * valor_quindin)
print('Paulo, hoje a padaria faturou: R$', total_faturado)