# Construa uma função que desenhe um retângulo usando os caracteres ‘+’ ,
# ‘−’ e ‘| ‘. Esta função deve receber dois parâmetros, linhas e colunas, sendo
# que o valor por omissão é o valor mínimo igual a 1 e o valor máximo é 20. Se
# valores fora da faixa forem informados, eles devem ser modificados para
# valores dentro da faixa


tabuleiro = [[] + ['|' * 10]] 
# linha = int(input('Digite a linha: '))
# while linha < 0 or linha > 19:  
#     linha = int(input('Digite a linha de 0 a 19: '))
   
# coluna = int(input('Digite a coluna: ')) 
# while coluna < 0 or coluna > 19:
#     coluna = int(input('Digite a coluna de 0 a 19: '))

# retangulo = [['-' for i in range(linha -1)] '|' for i in range(coluna)]

# a = '\n|' *10
# b = '-' *20
# c = '\n|' *10
# d = '-'*20
# e = '+'
# e = b + c + d 
# print(e)

lista = [[-,-,-],[|,+,|],[|,+,|],[|,+,|],[-,-,-]]

for i in lista:
    print(i)


# print(lista[0][1])