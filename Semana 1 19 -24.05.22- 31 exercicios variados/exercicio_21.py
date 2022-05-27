# Uma pessoa resolveu fazer uma aplicação em uma poupança programada. Para calcular seu 
# rendimento, ela deverá fornecer o valor constante da aplicação mensal, a taxa e o número de meses. 
# Sabendo-se que a fórmula usada para este cálculo é:
# onde:
#• i = taxa
#• P = aplicação mensal
#• n= número de meses
# Crie um programa que receba os coeficientes necessários e realize o cálculo.
aplicacao_mensal = float(input('Informe o valor do aporte mensal: R$ '))
numero_meses = int(input('Informe o numero de meses:'))
taxa = float(input('Informe a taxa de rendimento mensal:'))
rendimento = taxa / 100
calculo_rendimento = aplicacao_mensal * (((1 + rendimento) ** numero_meses) - 1) / rendimento
print('O valor total do rendimento apos',numero_meses,'meses, é de: R$',calculo_rendimento)
