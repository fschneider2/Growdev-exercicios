# Crie um algoritmo que funcione como um jogo de loteria, conforme as seguintes
# regras:
# a) O algoritmo deve gerar três números aleatórios entre 0 e 9;
# b) O usuário deve fornecer um palpite com três números, também entre 0 e 9;
# c) Cada um dos palpites do usuário deve ser comparado com os números
# aleatórios, de acordo com a tabela abaixo:

#                 Números Correspondentes                              |Número de pontos

# Nenhum número coincidente                                            |0 ### 
# Acertar um número                                                    |10 ###
# Acertar dois números                                                 |100 
# Acertar os três números, mas não na mesma ordem em que foram gerados |1000                                                                    |
# Acertar três números na mesma ordem que os números aleatórios        |1.000.000 ###

import random

print('Loteria dos 3 palpites')
print(('$ $ ')*15)

print('Vamos jogar!!! Abaixo, informe seus 3 palpites de 0 a 9.')

n1 = int(input('Palpite 1: '))
while n1 < 0 or n1 > 9:
    n1 = int(input('Erro. Informe um numero de 0 - 9: '))

n2 = int(input('Palpite 2: '))
while n2 < 0 or n2 > 9:
    n2 = int(input('Erro. Informe um numero de 0 - 9: '))

n3 = int(input('Palpite 3: '))
while n3 < 0 or n3 > 9:
    n3 = int(input('Erro. Informe um numero de 0 - 9: '))
# para teste:
# aleatorio = [1, 2, 3]
aleatorio = random.sample(range(10), 3)

# a partir daqui, usei a ideia do colega Marcus Faustino. Ele me apresentou, dei mais uma pesquisada para entender bem e optei por utilizar. 
# 
#  Eu estava encontrando erros para localizar o de 100 e o de 1000 pontos,
#  e meus operadores logicos estavam resultando em muita informação, para resolver o de 10 pontos, usei tudo isso que esta a baixo por exemplo:

# elif n1 == al1 and n1 != al2 and n1 != al3 or n1 != al1 and n1 == al2 and n1 != al3 or n1 != al1 and n1 != al2 and n1 == al3 and n2 != al1 and n2 != al2 and n2 != al3 and n3 != al1 and n3 != al2 and n3 != al3:
#     print('Seus números: {}, {}, {} | Números sorteados: {}, {}, {}| Você acertou 1 número.' 
#                             ' - Ganhou 10 pontos!'.format(n1, n2, n3, al1, al2, al3))

# elif n2 == al1 and n2 != al2 and n2 != al3 or n2 != al1 and n2 == al2 and n2 != al3 or n2 != al1 and n2 != al2 and n2 == al3 and n1 != al1 and n1 != al2 and n1 != al3 and n3 != al1 and n3 != al2 and n3 != al3:
#     print('Seus números: {}, {}, {} | Números sorteados: {}, {}, {}| Você acertou 1 número.' 
#                             ' - Ganhou 10 pontos!'.format(n1, n2, n3, al1, al2, al3))

# elif n3 == al1 and n3 != al2 and n3 != al3 or n3 != al1 and n3 == al2 and n3 != al3 or n3 != al1 and n3 != al2 and n3 == al3 and n1 != al1 and n1 != al2 and n1 != al3 and n2 != al1 and n2 != al2 and n2 != al3:
#     print('Seus números: {}, {}, {} | Números sorteados: {}, {}, {}| Você acertou 1 número.' 
#                             ' - Ganhou 10 pontos!'.format(n1, n2, n3, al1, al2, al3))


# se criou as variaveis dos erros que serão encontrados e foi dado um valor a ela
erro1 = 10
erro2 = 10
erro3 = 10

# se usou o try e o except para tratar esses erros, e com a numeração resultante, teremos a infomração de quantos acertos existem dentro da compração entre os informados pelo usario e os 3 sorteados.

try:
    x1 = aleatorio.index(n1)
except ValueError:
    erro1 = 0

try:
    x2 = aleatorio.index(n2)
except ValueError:
    erro2 = 0

try:
    x3 = aleatorio.index(n3)
except ValueError:
    erro3 = 0

if erro1 + erro2 + erro3 == 0:
    print('Seus números: {}, {}, {} | Números sorteados: {}| Você errou os 3 números.' 
                            ' - Ganhou 0 pontos!'.format(n1, n2, n3, aleatorio))
    exit()

elif erro1 + erro2 + erro3 == 10:
    print('Seus números: {}, {}, {} | Números sorteados: {} | Você acertou 1 número.' 
                            ' - Ganhou 10 pontos!'.format(n1, n2, n3, aleatorio))
    exit()

elif erro1 + erro2 + erro3 == 20:
    print('Seus números: {}, {}, {} | Números sorteados: {} | Você acertou 2 número.' 
                            ' - Ganhou 100 pontos!'.format(n1, n2, n3, aleatorio))
    exit()

x1 = aleatorio.index(n1)
x2 = aleatorio.index(n2)
x3 = aleatorio.index(n3)

# agora estou tratando dos 2 primeiros premios, de quem acertou os 3 numeros, x1 ==0 and x2 ==1 equivalem a posição deles dentro da lista.
if x1 == 0 and x2 == 1 and x3 == 2:
    print('Seus números: {}, {}, {} | Números sorteados: {} | Você acertou os 3 números na ordem sorteada' 
                            ' - Ganhou 1.000.000 pontos!'.format(n1, n2, n3, aleatorio))

elif (x1 <= 2 and x1 >= 0) and (x2 <= 2 and x2 >= 0) and x3 <= 2 and x3 >= 0:
    print('Seus números: {}, {}, {} | Números sorteados: {}| Você acertou 3 números fora de ordem.' 
                            ' - Ganhou 1000 pontos!'.format(n1, n2, n3, aleatorio))

