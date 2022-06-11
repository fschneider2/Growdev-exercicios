# A padaria do Paulo vende pão francês a R$0.75, pão doce a R$0.85 
# e quindim a R$1.50. Crie um algoritmo que pergunte quantas unidades de cada produto 
# foram vendidas pelo Paulo num dia e calcule o total faturado.

# Modificação 2 – Paulo tem o hábito de guardar 10% de tudo que fatura numa caderneta de poupança, 
# para eventuais necessidades no futuro. Sabendo disso, modifique o algoritmo que você criou 
# para que ele informe quanto do total faturado deve ser poupado..

print('Olá Paulo, vamos calcular o total faturado pela sua padaria no dia de hoje,informe a baixo a quantidade de cada item vendido e após o valor.')
pao_frances = int(input('Pão Frances: '))
pao_doce = int(input('Pão Doce: '))
quindin = int(input('Quindin: '))
valor_pao_frances = float(input('Valo do pão frances: '))
valor_pao_doce = float(input('Valo do pão doce: '))
valor_quindin = float(input('Valo do quindin: '))
total_faturado = (pao_frances * valor_pao_frances) + (pao_doce * valor_pao_doce) + (quindin * valor_quindin)
print('Paulo, hoje a padaria faturou: R$', total_faturado)
poupanca = (total_faturado / 100) * 10
print('e Voce deve depositar: R$', poupanca, 'na sua caderneta de poupança')