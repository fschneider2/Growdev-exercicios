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

# ainda em testes:
al1 = 1
al2 = 2
al3 = 3

# aleatorio1 = random.randint(0, 9)
# aleatorio2 = random.randint(0, 9)
# aleatorio3 = random.randint(0, 9)

# 1.000.000 ###
if n1 == al1 and n2 == al2 and n3 == al3:
    print('Seus números: {}, {}, {} | Números sorteados: {}, {}, {}| Você acertou os 3 números na ordem sorteada' 
                            ' - Ganhou 1.000.000 pontos!'.format(n1, n2, n3, al1, al2, al3))

# 1000
elif n1 == al1 and n1 != al2 and n1 != al3 or n1 != al1 and n1 == al2 and n1 != al3 or n1 != al1 and n1 != al2 and n1 == al3 and n2 != al1 and n2 != al2 and n2 != al3 and n3 != al1 and n3 != al2 and n3 != al3:
    print('Seus números: {}, {}, {} | Números sorteados: {}, {}, {}| Você acertou 3 números fora de ordem.' 
                            ' - Ganhou 1000 pontos!'.format(n1, n2, n3, al1, al2, al3))

elif n2 == al1 and n2 != al2 and n2 != al3 or n2 != al1 and n2 == al2 and n2 != al3 or n2 != al1 and n2 != al2 and n2 == al3 and n1 != al1 and n1 != al2 and n1 != al3 and n3 != al1 and n3 != al2 and n3 != al3:
    print('Seus números: {}, {}, {} | Números sorteados: {}, {}, {}| Você acertou 3 números forma de ordem.' 
                            ' - Ganhou 1000 pontos!'.format(n1, n2, n3, al1, al2, al3))

elif n3 == al1 and n3 != al2 and n3 != al3 or n3 != al1 and n3 == al2 and n3 != al3 or n3 != al1 and n3 != al2 and n3 == al3 and n1 != al1 and n1 != al2 and n1 != al3 and n2 != al1 and n2 != al2 and n2 != al3:
    print('Seus números: {}, {}, {} | Números sorteados: {}, {}, {}| Você acertou 3 números fora de ordem.' 
                            ' - Ganhou 1000 pontos!'.format(n1, n2, n3, al1, al2, al3))

# 10 
elif n1 == al1 and n1 != al2 and n1 != al3 or n1 != al1 and n1 == al2 and n1 != al3 or n1 != al1 and n1 != al2 and n1 == al3 and n2 != al1 and n2 != al2 and n2 != al3 and n3 != al1 and n3 != al2 and n3 != al3:
    print('Seus números: {}, {}, {} | Números sorteados: {}, {}, {}| Você acertou 1 número.' 
                            ' - Ganhou 10 pontos!'.format(n1, n2, n3, al1, al2, al3))

elif n2 == al1 and n2 != al2 and n2 != al3 or n2 != al1 and n2 == al2 and n2 != al3 or n2 != al1 and n2 != al2 and n2 == al3 and n1 != al1 and n1 != al2 and n1 != al3 and n3 != al1 and n3 != al2 and n3 != al3:
    print('Seus números: {}, {}, {} | Números sorteados: {}, {}, {}| Você acertou 1 número.' 
                            ' - Ganhou 10 pontos!'.format(n1, n2, n3, al1, al2, al3))

elif n3 == al1 and n3 != al2 and n3 != al3 or n3 != al1 and n3 == al2 and n3 != al3 or n3 != al1 and n3 != al2 and n3 == al3 and n1 != al1 and n1 != al2 and n1 != al3 and n2 != al1 and n2 != al2 and n2 != al3:
    print('Seus números: {}, {}, {} | Números sorteados: {}, {}, {}| Você acertou 1 número.' 
                            ' - Ganhou 10 pontos!'.format(n1, n2, n3, al1, al2, al3))

# 0 ###
elif n1 != al1 and n1 != al2 and n1 != al3 and n2 != al1 and n2 != al2 and n2 != al3 and n3 != al1 and n3 != al2 and n3 != al3:
    print('Seus números: {}, {}, {} | Números sorteados: {}, {}, {}| Você errou os 3 números.' 
                            ' - Ganhou 0 pontos!'.format(n1, n2, n3, al1, al2, al3))