# Crie um programa que calcule a folha de pagamento de uma empresa, conforme as instruções a seguir:

# a) O usuário pode inserir continuamente os nomes dos empregados até que escolha a opção de finalizar o informe de dados; V

# b) Após informar o nome de cada empregado, o usuário deverá informar o valor do salário da hora trabalhada desse empregado e quantas horas ele trabalhou; V

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
# Acima de R$ 8.000,00                  20%

import os

os.system('clear')

informações = {'Nome': nomes, 'Salario'}
emp = []
qHoras = []
s_bruto = []
s_liquido = []
imp = []

p1 = 10
p2 = 13
p3 = 16
p4 = 20

finalPrograma = False

def calc_salario(valor_salario, quantidade_horas):
    salario_bruto = valor_salario * quantidade_horas
    s_bruto.append(salario_bruto)

    if salario_bruto < 3.000:
        imposto = salario_bruto * 0.10
        imp.append(imposto)
        salario_liquido = salario_bruto - imposto
        s_liquido.append(salario_liquido)

    elif salario_bruto >= 3.000 and salario_bruto < 5.500:
        imposto = salario_bruto * 0.13
        imp.append(imposto)
        salario_liquido = salario_bruto - imposto
        s_liquido.append(salario_liquido)

    elif salario_bruto >= 5.500 and salario_bruto < 8.000:
        imposto = salario_bruto * 0.16
        imp.append(imposto)
        salario_liquido = salario_bruto - imposto
        s_liquido.append(salario_liquido)

    else: 
        imposto = salario_bruto * 0.20
        imp.append(imposto)
        salario_liquido = salario_bruto - imposto
        s_liquido.append(salario_liquido)

print('\nVamos calcular a folha de pagamento: informe a baixo nome, valor da hora e quantidade de horas trabalhadas. Para encerrar, digite exit no campo nome do funcionario\n')

while finalPrograma == False:
    
    os.system('clear')

    nomes = str(input('\nNome do funcionario: '))
    valor = float(input('\nValor hora: R$ '))
    hora = float(input('\nQuantidade de horas trabalhadas: '))
    sal = calc_salario(valor, hora)
    print('\nFuncionario {nomes}:')
    print(f'\nSalario Bruto: R$ {salario_bruto}')


    

    os.system('clear')
    if nomes == '0':
        finalPrograma = True

