# A prefeitura de uma cidade fez uma pesquisa entre seus habitantes,
# coletando dados sobre o salário e número de filhos. A prefeitura deseja
# saber:
# a) média do salário da população;
# b) média do número de filhos;
# c) maior salário;
# d) percentual de pessoas com salário até R$2000,00.
# Escreva um programa que receba as informações necessárias de 5 pessoas
# conforme a descrição e responda às questões a, b, c e d anteriores.

# defini as listas, o contador e o contador para saber qual o menor salario. 
# Caso queira, pode substituir o contador por um input, assim, 
# pode informar quantas pessoas vão responder a pesquisa.

contador = 1
salmenor2000 = 0
lista_salario = []
lista_filhos = []

# traduzindo: enquanto o contador for igual ou menor que 5, 
# ele vai solicitar o salario e quantos filhos a pessoa tem, 
# ele vai também armazenar essas informações nas listas, pois foi o que eu pedi para ele fazer 
# quando usei o .append
# Também vai atualizando os contadores 

while contador <= 5:
    salario = float(input('Informe seu salario: R$ '))
    if salario <= 2000:
        salmenor2000 += 1
    lista_salario.append(salario)
    filhos = int(input('Informe quantos filhos você possui: '))
    lista_filhos.append(filhos)
    contador += 1
# aqui fiz os calculos, a base de muita pesquisa na internet

media_salario = sum(lista_salario) / len(lista_salario)
media_filhos = sum(lista_filhos) / len(lista_filhos)
percent_menor2000 = (salmenor2000 * 100) / len(lista_salario)

# E aqui as saidas, podia usar tudo em uma unica linha,
#  mas gostei de usar assim também, fica mais facil de arrumar um erro de saida, e esse codigo foi dificil. 
print(f'A média dos salarios é : R$ {media_salario}')
print(f'A média de filhos por pessoa é : {media_filhos}')
print(f'{percent_menor2000}% delas ganham até R$ 2000,00')
print(f'O maior salario é: R$ {max(lista_salario)}')