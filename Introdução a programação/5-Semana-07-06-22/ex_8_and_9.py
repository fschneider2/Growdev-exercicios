# Crie uma estrutura bidimensional utilizando listas com sublistas para representar um tabuleiro (1 lista com 20 elementos e cada elemento é uma
# lista de 20 elementos, tabuleiro 20x20). Cada posição irá armazenar 1 valor numérico que significa:

# 0 - Água

# 1 - Navio

# Para cada posição escolha esses valores aleatoriamente, respeitando a regra de que não podem existir mais de 20 navios no tabuleiro. Após os valores
# serem distribuídos, o programa deve pedir ao usuário uma posição do tabuleiro e informar se ele acertou um navio ou água e repetir o procedimento
# até que o usuário derrote todos os navios ou chegue ao limite de 35 tentativas.

# Modifique o programa anterior para exibir as seguintes estatísticas.
# a) Acertos em água
# b) Acertos em Navios
# c) Porcentagem de acertos em água
# d) Porcentagem de acertos em Navios
# e) Acertos ininterruptos (maior quantidade de acertos em sequência)

import os
from random import randint
from time import sleep

os.system('clear')

chances = 0
acertos_navio = 0
acertos_agua = 0
acertos_seguidos = 0
seguidos = 1

tabuleiro = [[0 for i in range(20)] for i in range(20)] # estou criando  20 listas com 20 x o numero 0 dentro de cada uma

for linha in range(20): # acrescento os navios ao tabuleiro 
    coluna = randint(0,19)
    tabuleiro[linha][coluna] = 1

print('----Vamo jogar!----')

print(f'\nVocê possui 35 chances para acertar os 20 navios que estão distribuidos no tabuleiro, '
                            'o tabuleiro possui 20 linhas e 20 colunas, para jogar informe a linha e a coluna.\n')
print(tabuleiro)
sleep(4)
os.system('clear')

while chances < 35 and acertos_navio <= 20: # delimito o tempo de execução
   
    linha = int(input('Digite a linha: '))
    while linha < 0 or linha > 19:  # crio um laço para impedir o usuario de informar uma cordenada inexistente
        linha = int(input('Digite a linha de 0 a 19: '))
   
    coluna = int(input('Digite a coluna: ')) # solicito a entrada de coordenadas
    while coluna < 0 or coluna > 19:
        coluna = int(input('Digite a coluna de 0 a 19: '))
    
    if tabuleiro[linha][coluna] == 1: # é feita a analize, se acertou calcula como acerto 
        print('\nParabéns, você acertou um navio!\n')
        acertos_navio += 1
        chances += 1

        if seguidos > 0: # para contabilizar os acertos em sequencia 
            if  acertos_seguidos <= seguidos:
                hits_in_sequenced = seguidos
        seguidos += 1

        tabuleiro[linha][coluna] = 0 # para que o usuario não consiga incluir duas vezes a mesma coordenada, sendo que, ao ele acertar, o 1 será substituido por 0, no tabuleiro.

        sleep(1.5)
        os.system('clear')

        print(f'\nAinda faltam {20 - acertos_navio} navios e você ainda possui {35 - chances} tentativas.\n')

    else: # caso o palpite caia na agua (0), contabiliza e zera o contador de acertos seguidos.
        chances += 1
        acertos_agua += 1 
        seguidos = 0
        print(f'\nVocê acertou a água!\n')

        sleep(1.5)
        os.system('clear')

        print(f'\nAinda faltam {20 - acertos_navio} navios e você ainda possui {35 - chances} tentativas.\n')

porcent_agua = (acertos_agua * 100) / chances
porcent_navio = (acertos_navio * 100) / chances

print(f'\nVocê acertou {acertos_agua:2} na água')
print(f'\nVocê acertou {acertos_navio:2} em navios')
print(f'\nAcertando {porcent_agua} % das vezes na água e {porcent_navio}% em navios.')
print(f'\nSua maior serie de acertos em sequencia foi {acertos_seguidos} acertos seguidos.')