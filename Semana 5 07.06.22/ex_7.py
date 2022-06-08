# Crie um programa que calcule a folha de pagamento de uma empresa, conforme as instruções a seguir:

# a) O usuário pode inserir continuamente os nomes dos empregados até que escolha a opção de finalizar o informe de dados;

# b) Após informar o nome de cada empregado, o usuário deverá informar o valor do salário da hora trabalhada desse empregado e quantas horas ele trabalhou;

# c) O programa deve calcular o salário bruto de cada empregado, a percentagem de imposto retido na fonte (com base na tabela abaixo),
# o valor do imposto retido na fonte e o salário líquido (pagamento bruto menos imposto retido na fonte);

# d) Depois que o usuário inserir os dados do último empregado, o programa deve exibir o salário bruto, salário líquido, percentual de
# imposto e valor do imposto para cada funcionário;

# e) Por último, o programa deve exibir a soma de todas as horas trabalhadas, o total da folha de pagamento bruta, o total de imposto e
# a folha de pagamento líquida total.

# Percentuais de imposto
# Salário bruto                         Percentual
# Até R$ 2.999,99                       10%
# Entre R$ 3.000,00 e R$ 5.499,99       13%
# Entre R$ 5.500,00 e R$ 7.999,99       16%
# Acima de R$ 8.000,00                  20

import os
os.system('clear')

