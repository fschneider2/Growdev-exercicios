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
from time import sleep
os.system('clear')

empregado = []
quantidade_horas = []
salario_bruto = []
salario_liquido = []
valor_imposto = []
percent_imposto = []
encerrar = 0 

print('\nVamos calcular a folha de pagamento: informe a baixo niterableome, valor da hora e quantidade de horas trabalhadas.')

while encerrar == 0:
    nome = input('\nNome do funcionario: ')
    empregado.append(nome)
    valor = float(input('\nValor hora: R$ '))
    hora = float(input('\nQuantidade de horas trabalhadas: '))
    quantidade_horas.append(hora)

    sleep(0.5)
    os.system('clear')

    bruto = valor * hora
    salario_bruto.append(bruto)

    if bruto < 3000:
        imposto = bruto * 0.10
        valor_imposto.append(imposto)
        liquido = bruto - imposto
        salario_liquido.append(liquido)
        percent_imposto = 10
        
    elif bruto >= 3000 and bruto < 5500:
        imposto = bruto * 0.13
        valor_imposto.append(imposto)
        liquido = bruto - imposto
        salario_liquido.append(liquido)
        percent_imposto = 13
            
    elif bruto >= 5500 and bruto < 8000:
        imposto = bruto * 0.16
        valor_imposto.append(imposto)
        liquido = bruto - imposto
        salario_liquido.append(liquido)
        percent_imposto = 16
            
    else: 
        imposto = bruto * 0.20
        valor_imposto.append(imposto)
        liquido = bruto - imposto
        salario_liquido.append(liquido)
        percent_imposto = 20

    print(f'\nFolha do funcionario {nome}:')
    print(f'\nSalario Bruto: R$ {salario_bruto}')
    print(f'\nImposto para este funcionario é {percent_imposto} %, que equivale a: R$ {valor_imposto} ')
    print(f'\nSalario Liquido: R$ {salario_liquido}')

    sair = int(input('\nPara encerrar digite [0], para continuar digite [1]: '))
    if sair == 0:
        encerrar +=1
    else:
        pass

    sleep(0.5)
    os.system('clear')

print('--------------Programa encerrado--------------')
print('\nInformações da folha de pagameto: ')
print(f'\nHoras totais trabalhadas: {sum(quantidade_horas)}')
print(f'\nTotal folha de pagamento bruta: R$ {sum(salario_bruto)}')
print(f'\nTotal de impostos: R$ {sum(valor_imposto)}')
print(f'\nFolha de pagamento liquida total: {sum(salario_liquido)}')
    

