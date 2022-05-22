# A padaria do Paulo vende pão francês a R$0.75, pão doce a R$0.85 
# e quindim a R$1.50. Crie um algoritmo que pergunte quantas unidades de cada produto 
# foram vendidas pelo Paulo num dia e calcule o total faturado.

# Modificação 3 – Modifique o algoritmo para que, antes de calcular quanto deve ser guardado na 
# poupança, ele desconte o valor do imposto devido, que é de 5%.
# 

print('Olá Paulo, vamos calcular o total faturado pela sua padaria no dia de hoje,informe a baixo a quantidade de cada item vendido e após o valor.')
pao_frances = int(input('Pão Frances: '))
pao_doce = int(input('Pão Doce: '))
quindin = int(input('Quindin: '))
valor_pao_frances = float(input('Valo do pão frances: '))
valor_pao_doce = float(input('Valo do pão doce: '))
valor_quindin = float(input('Valo do quindin: '))
total_faturado = (pao_frances * valor_pao_frances) + (pao_doce * valor_pao_doce) + (quindin * valor_quindin)
imposto = (total_faturado / 100) * 5
print('Paulo, hoje a padaria faturou: R$', total_faturado, 'e o imposto é: R$', imposto)
poupanca = (total_faturado - imposto) / 100 * 10
print('Voce deve depositar: R$', poupanca, 'na sua caderneta de poupança.')