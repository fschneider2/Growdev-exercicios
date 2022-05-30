# As Organizações XTC resolveram dar um aumento de salário aos seus
# colaboradores e lhe contrataram para desenvolver o programa que calcula os
# reajustes. Faça um programa que recebe o salário de um colaborador e o
# reajuste segundo o seguinte critério, baseado no salário atual:
# a) salários até R$ 280,00 (incluindo): aumento de 20%
# b) salários entre R$ 280,00 e R$ 700,00: aumento de 15%
# c) salários entre R$ 700,00 e R$ 1500,00: aumento de 10%
# d) salários de R$ 1500,00 em diante: aumento de 5%
# Após o aumento ser realizado informe na tela:
# a) o salário antes do reajuste;
# b) o percentual de aumento aplicado;
# c) o valor do aumento;
# d) o novo salário, após o aumento.

print('Calculo de aumento de salario, informe o salario atual que farei o calculo: ')

sal_atual = float(input('R$ '))

perc_aumento = 0
if sal_atual <= 280:
    perc_aumento = 20
elif sal_atual > 280 and sal_atual <= 700:
    perc_aumento = 15
elif sal_atual > 700 and sal_atual <= 1500:
    perc_aumento = 10
elif sal_atual >= 1500:
    perc_aumento = 5

valor_aumento = (sal_atual / 100) * perc_aumento
novo_salario = sal_atual + valor_aumento

if sal_atual <= 280:
    print('Para o salario R$ {}, foi aplicado {} % de ajuste, resultando'
    ' em R$ {:.4} de aumento | O novo salario é de: R$ {}'.format(sal_atual, perc_aumento, valor_aumento, novo_salario))

elif sal_atual > 280 and sal_atual <= 700:
    print('Para o salario R$ {}, foi aplicado {} % de ajuste, resultando'
    ' em R$ {:.4} de aumento | O novo salario é de: R$ {}'.format(sal_atual, perc_aumento, valor_aumento, novo_salario))

elif sal_atual > 700 and sal_atual <= 1500:
    print('Para o salario R$ {}, foi aplicado {} % de ajuste, resultando'
    ' em R$ {:.4} de aumento | O novo salario é de: R$ {}'.format(sal_atual, perc_aumento, valor_aumento, novo_salario))

elif sal_atual >= 1500:
    print('Para o salario R$ {}, foi aplicado {} % de ajuste, resultando'
    ' em R$ {:.4} de aumento | O novo salario é de: R$ {}'.format(sal_atual, perc_aumento, valor_aumento, novo_salario))